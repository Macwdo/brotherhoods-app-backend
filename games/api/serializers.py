from rest_framework.serializers import ModelSerializer

from games.models import Game


class GameSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Game
