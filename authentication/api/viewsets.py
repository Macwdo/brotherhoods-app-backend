from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class ApiAuthMixin:
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class AuthenticedModelViewSet(ApiAuthMixin, ModelViewSet):
    class Meta:
        abstract = True
