from datetime import datetime
from django.utils import timezone


from games.models import Game


class GameMixins:
    def create_game(self, game_day: datetime = timezone.now()):
        return Game.objects.create(game_day=game_day)
