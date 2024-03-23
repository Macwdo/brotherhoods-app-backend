from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from app_platform.api.v1.serializers import PlayerSerializer, PlayerBillSerializer, PlayersGamesSerializer
from app_platform.models import Player, PlayerBill, PlayersGames



class PlayerViewSet(ModelViewSet):
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