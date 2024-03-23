from rest_framework.serializers import ModelSerializer

from app_platform.api.v1.serializers import GameSerializer
from app_platform.models import PlayersGames, Player, PlayerBill


class PlayerSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Player


class PlayerBillSerializer(ModelSerializer):
    player = PlayerSerializer(many=False, read_only=True)

    class Meta:
        fields = "__all__"
        model = PlayerBill


class PlayersGamesSerializer(ModelSerializer):
    game = GameSerializer(many=False, read_only=True)
    player = PlayerSerializer(many=False, read_only=True)

    class Meta:
        fields = "__all__"
        model = PlayersGames
