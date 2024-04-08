from project.api.viewsets.base_viewsets import BaseModelViewSet
from players.api.serializers import (
    PlayerSerializer,
    PlayerBillSerializer,
    PlayersGamesSerializer,
)
from players.models import Player, PlayerBills, PlayersGames


class PlayerRelationModelViewSet(BaseModelViewSet):
    def get_queryset(self):
        return super().get_queryset().filter(player_id=self.kwargs["player_pk"])

    def perform_create(self, serializer):
        serializer.save(player_id=self.kwargs["player_pk"])


class PlayerViewSet(BaseModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerBillViewSet(PlayerRelationModelViewSet):
    queryset = PlayerBills.objects.all()
    serializer_class = PlayerBillSerializer


class PlayersGamesViewSet(PlayerRelationModelViewSet):
    queryset = PlayersGames.objects.all()
    serializer_class = PlayersGamesSerializer
