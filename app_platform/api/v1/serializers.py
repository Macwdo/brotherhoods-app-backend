from rest_framework.serializers import ModelSerializer

from app_platform.models import PlayersGames, Player, PlayerBill, Game


class PlayerSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Player


class PlayerBillSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = PlayerBill


class GameSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Game


class PlayersGamesSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = PlayersGames
