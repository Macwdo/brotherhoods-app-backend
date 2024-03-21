from rest_framework.serializers import ModelSerializer


class PlayerSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"


class PlayerBillSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"


class GameSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"


class PlayersGamesSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
