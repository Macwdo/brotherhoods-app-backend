import pytest
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import SimpleTestCase
from django.urls import reverse

from authentication.tests.mixins.auth_mixin import AuthMixin
from games.api.serializers import GameSerializer
from games.models import Game
from games.services import GameService
from games.tests.mixins.game_mixins import GameMixins


class GameViewSetAuthTest(APITestCase):
    def setUp(self) -> None:
        super().setUp()
        self.__user_data = {"username": "username", "password": "password"}
        self.__user = User.objects.create(**self.__user_data, is_active=True)

    @pytest.mark.viewset
    @pytest.mark.auth
    def test_get_game_by_unauthenticated_user_should_return_401(self):
        url = reverse("games:game-list")

        response = self.client.get(url)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.viewset
    @pytest.mark.auth
    def test_get_game_by_authenticated_user_should_return_200(self):
        url = reverse("games:game-list")
        self.client.force_authenticate(user=self.__user)
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK


class GameViewSetUrlsTest(SimpleTestCase):
    @pytest.mark.url
    def test_games_viewset_reverse_list_url(self):
        reverse_url = "games:game-list"
        expected_url = "/api/games/"
        assert reverse(reverse_url) == expected_url

    @pytest.mark.url
    def test_games_viewset_reverse_detail_url(self):
        reverse_url = "games:game-detail"
        expected_url = "/api/games/1/"
        assert reverse(reverse_url, args=(1,)) == expected_url

    @pytest.mark.url
    def test_week_games_reverse_url(self):
        reverse_url = "games:game-week-games"
        expected_url = "/api/games/week-games/"
        assert reverse(reverse_url) == expected_url

    @pytest.mark.url
    def test_create_week_games_reverse_url(self):
        reverse_url = "games:game-create-week-game"
        expected_url = "/api/games/week/"
        assert reverse(reverse_url) == expected_url


class GameViewSetTest(APITestCase, GameMixins, AuthMixin):
    def setUp(self) -> None:
        super().setUp()

        self.__user_data = {"username": "username", "password": "password"}
        self.__user = User.objects.create(**self.__user_data, is_active=True)
        self.client.force_authenticate(user=self.__user)
        self.__service = GameService()

    @pytest.mark.viewset
    def test_get_week_games(self):
        url = reverse("games:game-week-games")
        previous_game = self.__service.create_week_game()
        next_game = self.__service.create_week_game()

        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert (
            response.data.get("next") == GameSerializer(instance=next_game).data
        )
        assert (
            response.data.get("previous")
            == GameSerializer(instance=previous_game).data
        )

    @pytest.mark.viewset
    def test_create_previous_week_game(self):
        url = reverse("games:game-create-week-game")

        response = self.client.post(url)

        assert response.status_code == status.HTTP_200_OK

        created_game = Game.objects.get_previous_week_game()
        pk = response.data.get("id")
        game_by_response_id = Game.objects.get(id=pk)
        assert game_by_response_id == created_game

    @pytest.mark.viewset
    def test_create_previous_and_next_week_game(self):
        url = reverse("games:game-create-week-game")

        self.__service.create_week_game()
        next_week_game_response = self.client.post(url)

        assert next_week_game_response.status_code == status.HTTP_200_OK

        next_week_game = Game.objects.get_next_week_game()
        id_next_week_game = next_week_game_response.data.get("id")
        next_week_game_by_response_id = Game.objects.get(id=id_next_week_game)

        assert next_week_game == next_week_game_by_response_id

    @pytest.mark.viewset
    def test_create_week_game_should_raise_an_error_when_week_games_already_exists(self):
        self.__service.create_week_game()
        self.__service.create_week_game()

        url = reverse("games:game-create-week-game")
        response = self.client.post(url)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data.get("message") == "Não foi possível criar jogo da semana, já foi criado o da ultíma e da proxíma."



