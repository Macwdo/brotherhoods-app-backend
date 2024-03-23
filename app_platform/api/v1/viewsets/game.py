from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from app_platform.api.v1.serializers import GameSerializer
from app_platform.models import Game


class GameViewSet(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]
