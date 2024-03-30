from urllib.request import urlretrieve
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status

from authentication.tests.mixins.auth_mixin import AuthMixin
from authentication.types import LoginRequest


class PlayerViewSetTest(AuthMixin):
    def setUp(self):
        super().setUp()
        username, password = "username", "password"
        self.__user = User.objects.create(
            username=username, is_active=True, is_superuser=True, is_staff=True
        )
        self.__user.set_password(password)
        self.__user.save()

        self.__user_credentials = {"username": username, "password": password}


    def test_get_token(self):
        credentials = self.__user_credentials
        request = LoginRequest(**credentials)

        token = self.get_token(request=request)
        assert token.access is not None
        assert token.refresh is not None

    
    def test_refresh_token(self):
        credentials = self.__user_credentials
        request = LoginRequest(**credentials)
        token = self.get_token(request=request)
        url = reverse("token_refresh")

        response = self.client.post(url, data = {"refresh": token.refresh})
        assert response.status_code == status.HTTP_200_OK


    def test_authenticated_user_when_get_should_returns_200(self):
        url = reverse("players:player-list")
        credentials = self.__user_credentials
        request = LoginRequest(**credentials)

        token = self.get_token(request=request)
        auth_header = {"Authorization": f"Bearer {token.access}"}
        response = self.client.get(url, headers=auth_header)

        assert response.status_code == status.HTTP_200_OK

    def test_unauthenticated_user_when_get_should_returns_401(self):
        url = reverse("players:player-list")
        response = self.client.get(url)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
