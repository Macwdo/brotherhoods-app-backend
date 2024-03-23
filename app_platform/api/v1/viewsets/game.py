import logging

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from app_platform.services.game import GameService

from app_platform.api.v1.serializers import GameSerializer
from app_platform.models import Game
from app_platform.services.game import GameAlreadyExistsException

logger = logging.getLogger(__name__)


class GameViewSet(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["POST"], url_path="week")
    def create_week_game(self, request: Request):
        try:
            GameService().create_week_game()
            return Response(status=status.HTTP_200_OK)

        except GameAlreadyExistsException:
            data = {"message": "Não foi possível criar jogo da semana, já foi criado o da ultíma e da proxíma."}
            return Response(status=status.HTTP_400_BAD_REQUEST, data=data)
