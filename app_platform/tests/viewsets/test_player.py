from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from app_platform.tests.mixins.auth_mixin import AuthMixin
from app_platform.types.auth import LoginRequest


class PlayerViewSetTest(AuthMixin):

    def setUp(self):
        super().setUp()
        username, password = "username", "password"
        self.__user = User.objects.create(username=username, is_active=True, is_superuser=True, is_staff=True)
        self.__user.set_password(password)
        self.__user.save()

        self.__user_credentials = {
            "username": username,
            "password": password
        }

    def test_authenticated_user_when_get_should_returns_200(self):
        url = reverse("app_platform:player-list")
        credentials = self.__user_credentials
        request = LoginRequest(**credentials)

        token = self.get_token(request=request)
        auth_header = {"Authorization": f"Bearer {token.access_token}"}
        response = self.client.get(url, headers=auth_header)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
