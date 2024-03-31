import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status

from authentication.tests.mixins.auth_mixin import AuthMixin
from authentication.types import LoginRequest


class PlayerViewSetTest(AuthMixin):
    def setUp(self) -> None:
        super().setUp()
        username, password = "username", "password"
        self.__user = User.objects.create(
            username=username, is_active=True, is_superuser=True, is_staff=True
        )
        self.__user.set_password(password)
        self.__user.save()

        self.__user_credentials = {"username": username, "password": password}

    def test_player_viewset_reverse_list_url(self):
        reverse_url = "players:player-list"
        expected_url = "/api/players/"
        assert reverse(reverse_url) == expected_url

    def test_player_viewset_reverse_detail_url(self):
        reverse_url = "players:player-detail"
        expected_url = "/api/players/1/"
        assert reverse(reverse_url, args=(1,)) == expected_url

    @pytest.mark.auth
    def test_authenticated_user_when_get_should_returns_200(self):
        url = reverse("players:player-list")
        credentials = self.__user_credentials
        request = LoginRequest(**credentials)

        token = self.get_token(request=request)
        auth_header = {"Authorization": f"Bearer {token.access}"}
        response = self.client.get(url, headers=auth_header)

        assert response.status_code == status.HTTP_200_OK
