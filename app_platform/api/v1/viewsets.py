from rest_framework.viewsets import ModelViewSet

from app_platform.api.v1.serializers import (
    GameSerializer,
    PlayerBillSerializer,
    PlayerSerializer,
    PlayersGamesSerializer,
)
from app_platform.models import Game, Player, PlayerBill, PlayersGames


class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerBillViewSet(ModelViewSet):
    queryset = PlayerBill.objects.all()
    serializer_class = PlayerBillSerializer


class GameViewSet(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class PlayersGamesViewSet(ModelViewSet):
    queryset = PlayersGames.objects.all()
    serializer_class = PlayersGamesSerializer
