from django.utils import timezone
from decimal import Decimal
from django.test import SimpleTestCase
import pytest
from rest_framework import status

from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from players.models import PlayerBill
from players.tests.mixins.player_mixins import PlayerMixins


class PlayerBillsViewSetAuthTest(APITestCase):
    def setUp(self) -> None:
        super().setUp()
        self.__user_data = {"username": "username", "password": "password"}
        self.__user = User.objects.create(**self.__user_data, is_active=True)

    @pytest.mark.auth
    @pytest.mark.viewset
    def test_get_player_bills_by_authenticated_user_should_return_200(self):
        url = reverse("players:player-bills-list", args=(1,))
        self.client.force_authenticate(user=self.__user)
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.auth
    @pytest.mark.viewset
    def test_get_player_bills_by_unauthenticated_user_should_return_401(self):
        url = reverse("players:player-bills-list", args=(1,))

        response = self.client.get(url)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


class PlayerBillsViewSetUrlsTest(SimpleTestCase):
    @pytest.mark.url
    def test_player_bills_viewset_reverse_list_url(self):
        reverse_url = "players:player-bills-list"
        expected_url = "/api/players/1/bills/"
        assert reverse(reverse_url, args=(1,)) == expected_url

    @pytest.mark.url
    def test_player_bills_viewset_reverse_detail_url(self):
        reverse_url = "players:player-bills-detail"
        expected_url = "/api/players/1/bills/1/"
        assert reverse(reverse_url, args=(1, 1)) == expected_url


class PlayerBillsViewSet(APITestCase, PlayerMixins):
    
    def setUp(self) -> None:
        super().setUp()
        self.__user_data = {"username": "username", "password": "password"}
        self.__user = User.objects.create(**self.__user_data, is_active=True)
        
        self.client.force_authenticate(user=self.__user)

    def test_create_player_bill_should_be_related_from_player(self):
        player = self.create_player()
        url = reverse("players:player-bills-list", args=(player.id,))

        data = {
            "due_date": timezone.now(),
            "payed_date": timezone.now(),
            "payed_value": Decimal("92.43")
        }
        response = self.client.post(url, data=data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["player"]["id"] == player.id

        player_bill = PlayerBill.objects.get(id=response.data["id"])
        assert player_bill.player.id == response.data["player"]["id"]
    