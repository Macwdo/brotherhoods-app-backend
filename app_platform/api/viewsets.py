from rest_framework.viewsets import ModelViewSet

from app_platform.api.serializers import (
    GameSerializer,
    PlayerBillSerializer,
    PlayerSerializer,
    PlayersGamesSerializer,
)
from app_platform.models import Game, Player, PlayerBill, PlayersGames


class PlayerViewSet(ModelViewSet):
    queryset = Player
    serializer_class = PlayerSerializer
    ...


class PlayerBillViewSet(ModelViewSet):
    queryset = PlayerBill
    serializer_class = PlayerBillSerializer
    ...


class GameViewSet(ModelViewSet):
    queryset = Game
    serializer_class = GameSerializer
    ...


class PlayersGamesViewSet(ModelViewSet):
    queryset = PlayersGames
    serializer_class = PlayersGamesSerializer
    ...
