from django.utils import timezone
from django.test import SimpleTestCase
from freezegun import freeze_time
import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from players.tests.mixins.player_mixins import PlayerMixins


class PlayerViewSetAuthTest(APITestCase):
    def setUp(self) -> None:
        super().setUp()
        self.__user_data = {"username": "username", "password": "password"}
        self.__user = User.objects.create(**self.__user_data, is_active=True)

    @pytest.mark.auth
    @pytest.mark.api
    def test_get_players_by_authenticated_user_should_return_200(self):
        url = reverse("players:player-list")
        self.client.force_authenticate(user=self.__user)
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.auth
    @pytest.mark.api
    def test_get_players_by_unauthenticated_user_should_return_401(self):
        url = reverse("players:player-list")

        response = self.client.get(url)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


class PlayerViewSetUrlsTest(SimpleTestCase):
    @pytest.mark.url
    def test_player_viewset_reverse_list_url(self):
        reverse_url = "players:player-list"
        expected_url = "/api/players/"
        assert reverse(reverse_url) == expected_url

    @pytest.mark.url
    def test_player_viewset_reverse_detail_url(self):
        reverse_url = "players:player-detail"
        expected_url = "/api/players/1/"
        assert reverse(reverse_url, args=(1,)) == expected_url


class PlayerViewSetTest(PlayerMixins, APITestCase):
    def setUp(self) -> None:
        super().setUp()
        self.__user_data = {"username": "username", "password": "password"}
        self.__user = User.objects.create(**self.__user_data, is_active=True)

        self.client.force_authenticate(user=self.__user)

    @pytest.mark.api
    @freeze_time("2024-04-07T22:00:00-03:00")
    def test_create_player(self):
        url = reverse("players:player-list")
        data = {
            "name": "Test Name",
            "surname": "Test Surname",
            "alias": "Test Alias",
            "phone_number": "+552199231212",
            "is_monthly_player": True,
            "active": True,
            "birth_date": "2024-04-07",
            "email": "mail@mail.com",
        }

        response = self.client.post(url, data=data)

        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.api
    @freeze_time("2024-04-07T22:00:00-03:00")
    def test_player_list_response(self):
        player = self.create_player(birth_date=timezone.now())
        url = reverse("players:player-list")
        freezed_time = "2024-04-07T22:00:00-03:00"

        expected_response = {
            "id": player.id,
            "deleted": False,
            "deleted_at": None,
            "created_at": freezed_time,
            "updated_at": freezed_time,
            "name": player.name,
            "surname": "Test Surname",
            "alias": "Test Alias",
            "phone_number": "+552199231212",
            "is_monthly_player": True,
            "active": True,
            "birth_date": "2024-04-07",
            "email": "test_mail@email.co",
        }
        response = self.client.get(url)

        assert response.data["results"][0] == expected_response

    @pytest.mark.api
    @freeze_time("2024-04-07T22:00:00-03:00")
    def test_player_detail_response(self):
        player = self.create_player(birth_date=timezone.now())
        url = reverse("players:player-detail", args=(player.id,))
        freezed_time = "2024-04-07T22:00:00-03:00"

        expected_response = {
            "id": player.id,
            "deleted": False,
            "deleted_at": None,
            "created_at": freezed_time,
            "updated_at": freezed_time,
            "name": player.name,
            "surname": "Test Surname",
            "alias": "Test Alias",
            "phone_number": "+552199231212",
            "is_monthly_player": True,
            "active": True,
            "birth_date": "2024-04-07",
            "email": "test_mail@email.co",
        }
        response = self.client.get(url)

        assert response.data == expected_response

    @pytest.mark.api
    @freeze_time("2024-04-07T22:00:00-03:00")
    def test_update_player(self):
        player = self.create_player(birth_date=timezone.now())
        url = reverse("players:player-detail", args=(player.id,))
        data = {
            "name": "Test Name",
            "surname": "Test Surname",
            "alias": "Test Alias",
            "phone_number": "+552199231212",
            "is_monthly_player": True,
            "active": True,
            "birth_date": "2024-04-07",
            "email": "new_mail@mail.com",
        }

        response = self.client.put(url, data=data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["email"] == "new_mail@mail.com"

    @pytest.mark.api
    @freeze_time("2024-04-07T22:00:00-03:00")
    def test_delete_player(self):
        player = self.create_player(birth_date=timezone.now())
        url = reverse("players:player-detail", args=(player.id,))

        response = self.client.delete(url)

        player.refresh_from_db()
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert response.data is None
        assert player.deleted
        assert player.deleted_at == timezone.now()
