from rest_framework.serializers import ModelSerializer

from games.api.serializers import GameSerializer
from players.models import PlayersGames, Player, PlayerBills


class PlayerSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Player


class PlayerBillSerializer(ModelSerializer):
    player = PlayerSerializer(many=False, read_only=True)

    class Meta:
        fields = "__all__"
        model = PlayerBills


class PlayersGamesSerializer(ModelSerializer):
    game = GameSerializer(many=False, read_only=True)
    player = PlayerSerializer(many=False, read_only=True)

    class Meta:
        fields = "__all__"
        model = PlayersGames
