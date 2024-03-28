from django.db import transaction
from app_platform.models.game import Game
from app_platform.models.player import Player, PlayersGames


class GameAlreadyExistsException(Exception): ...


class GameService:
    def __init__(self):
        self.__repository = Game.objects
        self.__players_games_repository = PlayersGames.objects
        self.__player_repository = Player.objects

    @transaction.atomic
    def create_week_game(self) -> Game:
        last_game = self.__repository.get_last_game()
        if not last_game:
            game = self.__repository.create_previous_week_game()
            self.__add_all_monthly_players(game)
            return game

        next_game = self.__repository.get_next_game()
        if not next_game:
            game = self.__repository.create_next_week_game()
            self.__add_all_monthly_players(game)
            return game

        raise GameAlreadyExistsException()

    def __add_all_monthly_players(self, game):
        monthly_players = (
            self.__player_repository.get_monthly_players()
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
