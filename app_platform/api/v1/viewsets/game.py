import logging

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from app_platform.services.game_service import GameService

from app_platform.api.v1.serializers import GameSerializer
from app_platform.models import Game

logger = logging.getLogger(__name__)

class GameViewSet(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["POST"], url_path="week")
    def create_week_game(self, request: Request):
        try:
            game = GameService().create_week_game()
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            logger.error("Error trying to create a week game")
            raise
