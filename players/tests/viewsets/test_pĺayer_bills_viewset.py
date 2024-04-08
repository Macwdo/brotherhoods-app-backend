from django.utils import timezone
from decimal import Decimal
from django.test import SimpleTestCase
import pytest
from rest_framework import status

from freezegun import freeze_time
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from players.models import PlayerBills
from players.tests.mixins.player_mixins import PlayerMixins


class PlayerBillsViewSetAuthTest(APITestCase):
    def setUp(self) -> None:
        super().setUp()
        self.__user_data = {"username": "username", "password": "password"}
        self.__user = User.objects.create(**self.__user_data, is_active=True)

    @pytest.mark.auth
    @pytest.mark.api
    def test_get_player_bills_by_authenticated_user_should_return_200(self):
        url = reverse("players:player-bills-list", args=(1,))
        self.client.force_authenticate(user=self.__user)
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.auth
    @pytest.mark.api
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

    @pytest.mark.api
    def test_create_player_bill_should_be_related_from_player(self):
        player = self.create_player()
        url = reverse("players:player-bills-list", args=(player.id,))

        data = {
            "due_date": timezone.now(),
            "payed_date": timezone.now(),
            "payed_value": Decimal("92.43"),
        }
        response = self.client.post(url, data=data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["player"]["id"] == player.id

        player_bill = PlayerBills.objects.get(id=response.data["id"])
        assert player_bill.player.id == response.data["player"]["id"]

    @freeze_time("2024-04-07T22:00:00-03:00")
    @pytest.mark.api
    def test_player_bills_list_response(self):
        player = self.create_player(birth_date=timezone.now())

        bills = [
            self.create_player_bill(
                player, due_date=timezone.now(), payed_date=timezone.now()
            )
            for _ in range(11)
        ]

        url = reverse("players:player-bills-list", args=(player.id,))
        response = self.client.get(url)

        freezed_time = "2024-04-07T22:00:00-03:00"

        expected_response = {
            "count": 11,
            "total": 2,
            "previous": None,
            "next": f"http://testserver/api/players/{player.id}/bills/?page=2",
            "results": [
                {
                    "id": bills[0].id,
                    "player": {
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
                    },
                    "deleted": False,
                    "deleted_at": None,
                    "created_at": freezed_time,
                    "updated_at": freezed_time,
                    "due_date": freezed_time,
                    "payed_date": freezed_time,
                    "payed_value": "0.00",
                }
            ],
        }
        assert response.data["count"] == expected_response["count"]
        assert response.data["total"] == expected_response["total"]
        assert response.data["previous"] == expected_response["previous"]
        assert response.data["next"] == expected_response["next"]
        assert response.data["results"][0] == expected_response["results"][0]

    @pytest.mark.api
    @freeze_time("2024-04-07T22:00:00-03:00")
    def test_player_bills_detail_response(self):
        player = self.create_player(birth_date=timezone.now())
        player_bill = self.create_player_bill(
            player, due_date=timezone.now(), payed_date=timezone.now()
        )
        freezed_time = "2024-04-07T22:00:00-03:00"

        url = reverse(
            "players:player-bills-detail", args=(player.id, player_bill.id)
        )
        response = self.client.get(url)

        expected_response = {
            "id": player_bill.id,
            "player": {
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
            },
            "deleted": False,
            "deleted_at": None,
            "created_at": freezed_time,
            "updated_at": freezed_time,
            "due_date": freezed_time,
            "payed_date": freezed_time,
            "payed_value": f"{player_bill.payed_value:.2f}",
        }
        assert response.data == expected_response

    @pytest.mark.api
    @freeze_time("2024-04-07T22:00:00-03:00")
    def test_player_bills_update_response(self):
        player = self.create_player(birth_date=timezone.now())
        player_bill = self.create_player_bill(
            player, due_date=timezone.now(), payed_date=timezone.now()
        )
        freezed_time = "2024-04-07T22:00:00-03:00"

        url = reverse(
            "players:player-bills-detail", args=(player.id, player_bill.id)
        )
        data = {
            "due_date": freezed_time,
            "payed_date": freezed_time,
            "payed_value": "90.43",
        }
        response = self.client.put(url, data=data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["payed_value"] == "90.43"

    @pytest.mark.api
    @freeze_time("2024-04-07T22:00:00-03:00")
    def test_player_bills_delete_response(self):
        player = self.create_player(birth_date=timezone.now())
        player_bill = self.create_player_bill(
            player, due_date=timezone.now(), payed_date=timezone.now()
        )

        url = reverse(
            "players:player-bills-detail", args=(player.id, player_bill.id)
        )
        response = self.client.delete(url)

        player_bill.refresh_from_db()
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert player_bill.deleted
        assert player_bill.deleted_at == timezone.now()
