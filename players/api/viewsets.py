from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from players.api.serializers import (
    PlayerSerializer,
    PlayerBillSerializer,
    PlayersGamesSerializer,
)
from players.models import Player, PlayerBill, PlayersGames


class ApiAuthMixin:
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class AuthenticedModelViewSet(ModelViewSet, ApiAuthMixin):
    class Meta:
        abstract = True


class PlayerViewSet(AuthenticedModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticated]


class PlayerBillViewSet(ModelViewSet):
    queryset = PlayerBill.objects.all()
    serializer_class = PlayerBillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(player_id=self.kwargs["player_pk"])

    def perform_create(self, serializer):
        serializer.save(player_id=self.kwargs["player_pk"])


class PlayersGamesViewSet(ModelViewSet):
    queryset = PlayersGames.objects.all()
    serializer_class = PlayersGamesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(player_id=self.kwargs["player_pk"])

    def perform_create(self, serializer):
        serializer.save(player_id=self.kwargs["player_pk"])
