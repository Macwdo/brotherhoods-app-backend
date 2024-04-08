from django.urls import reverse
from django.test import TestCase
from project.types.auth import LoginRequest, TokenResponse


class AuthMixin(TestCase):
    def setUp(self) -> None:
        self.get_token_url = reverse("token_obtain_pair")
        self.refresh_token_url = reverse("token_refresh")

    def get_token(self, request: LoginRequest) -> TokenResponse:
        url = self.get_token_url
        response = self.client.post(url, data=request.model_dump())
        return TokenResponse(**response.json())
