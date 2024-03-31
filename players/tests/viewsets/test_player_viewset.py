from django.test import SimpleTestCase
import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class PlayerViewSetAuthTest(APITestCase):
    def setUp(self) -> None:
        super().setUp()
        self.__user_data = {"username": "username", "password": "password"}
        self.__user = User.objects.create(**self.__user_data, is_active=True)

    @pytest.mark.auth
    @pytest.mark.viewset
    def test_get_players_by_authenticated_user_should_return_200(self):
        url = reverse("players:player-list")
        self.client.force_authenticate(user=self.__user)
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.auth
    @pytest.mark.viewset
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


class PlayerViewSetTest:
    pass
