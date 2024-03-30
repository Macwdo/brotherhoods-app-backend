from __future__ import absolute_import
from rest_framework import serializers

from games.models import Game



class GameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Game

class WeekGamesSerializer(serializers.Serializer):
    next = GameSerializer(many=False)
    previous = GameSerializer(many=False)