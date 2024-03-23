from rest_framework.serializers import ModelSerializer

from app_platform.models import PlayersGames, Player, PlayerBill


class PlayerSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Player


class PlayerBillSerializer(ModelSerializer):
    class Meta:
        model = PlayerBill
        exclude = ["player"]


class PlayersGamesSerializer(ModelSerializer):
    class Meta:
        model = PlayersGames
        exclude = ["player"]
