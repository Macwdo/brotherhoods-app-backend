from django.db import transaction
from app_platform.models.game import Game
from app_platform.models.player import Player, PlayersGames

from app_platform.utils import get_next_wednesday_date


class GameService:
    def __init__(self):
        self.__repository = Game.objects
        self.__players_games_repository = PlayersGames.objects
        self.__player_repository = Player.objects

    @transaction.atomic
    def create_week_game(self) -> Game:
        next_wednesday_date = get_next_wednesday_date()
        game = self.__repository.create(game_day=next_wednesday_date)
        self.__add_all_monthly_players(game)
        return game

    def __add_all_monthly_players(self, game):
        monthly_players = (
            self.__player_repository
            .get_monthly_players()
            .get_active_players()
            .values("id", "is_monthly_player")
        )
        players_games_instances = [
            PlayersGames(
                game=game,
                player_id=player["id"],
                as_monthly_player=player["is_monthly_player"],
            )
            for player in monthly_players
        ]
        self.__players_games_repository.bulk_create(players_games_instances)
