import logging

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action

from authentication.api.viewsets import AuthenticedModelViewSet
from games.api.serializers import GameSerializer, WeekGamesSerializer
from games.models import Game

from games.services import GameService
from games.services import GameAlreadyExistsException

logger = logging.getLogger(__name__)


class GameViewSet(AuthenticedModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    service = GameService()

    @action(
        detail=False,
        methods=["GET"],
        url_path="week-games",
        url_name="week-games",
    )
    def get_week_games(self, request: Request):
        week_games = self.service.get_week_games()
        serializer = WeekGamesSerializer(week_games)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(
        detail=False,
        methods=["POST"],
        url_path="week",
        url_name="create-week-game",
    )
    def create_week_game(self, request: Request):
        try:
            game = self.service.create_week_game()
            serializer = GameSerializer(instance=game)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        except GameAlreadyExistsException:
            data = {
                "message": "Não foi possível criar jogo da semana, já foi criado o da ultíma e da proxíma."
            }
            return Response(status=status.HTTP_400_BAD_REQUEST, data=data)
