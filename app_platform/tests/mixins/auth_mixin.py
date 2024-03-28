from django.urls import reverse
from django.test import TestCase
from app_platform.types.auth import LoginRequest, TokenResponse
from django.test import Client

class AuthMixin(TestCase):
    def setUp(self):
        self.client = Client()
        self.get_token_url = reverse("token_obtain_pair")
        self.refresh_token_url = reverse("token_refresh")

    def get_token(self, request: LoginRequest):
        url = self.get_token_url
        response = self.client.post(url, data=request.model_dump())
        return response.json()

