import pytest
from datetime import timedelta
from django.utils import timezone
from django.test import TestCase

from games.models import Game
from games.tests.mixins.game_mixins import GameMixins


# WARN: SimpleTestCase are not allowed to use db from django
class GameModelTest(TestCase, GameMixins):

    @pytest.mark.model
    def test_get_month_games(self):
        self.create_game()
        self.create_game()
        date_for_out_of_month_game = timezone.now() - timedelta(weeks=5)
        game_out_of_month = self.create_game(date_for_out_of_month_game)

        games_from_current_month = Game.objects.get_month_games()
        assert game_out_of_month not in games_from_current_month

    @pytest.mark.model
    def test_game_str(self):
        game = self.create_game()
        assert str(game) == f"Game[id={game.id}, game_day={game.game_day.strftime('%d/%m/%Y')}]"

    @pytest.mark.model
    def test_game_repr(self):
        game = self.create_game()
        assert repr(game) == f"Game[id={game.id}, game_day={game.game_day.strftime('%d/%m/%Y')}]"