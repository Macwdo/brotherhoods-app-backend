from authentication.api.viewsets import AuthenticedModelViewSet
from players.api.serializers import (
    PlayerSerializer,
    PlayerBillSerializer,
    PlayersGamesSerializer,
)
from players.models import Player, PlayerBill, PlayersGames


class PlayerRelationModelViewSet(AuthenticedModelViewSet):
    def get_queryset(self):
        return self.queryset.filter(player_id=self.kwargs["player_pk"])

    def perform_create(self, serializer):
        serializer.save(player_id=self.kwargs["player_pk"])


class PlayerViewSet(AuthenticedModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerBillViewSet(PlayerRelationModelViewSet):
    queryset = PlayerBill.objects.all()
    serializer_class = PlayerBillSerializer


class PlayersGamesViewSet(PlayerRelationModelViewSet):
    queryset = PlayersGames.objects.all()
    serializer_class = PlayersGamesSerializer
