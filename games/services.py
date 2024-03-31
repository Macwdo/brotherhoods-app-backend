from django.db import transaction
from games.models import Game
from games.types import WeekGames
from players.models import Player, PlayersGames


class GameAlreadyExistsException(Exception): ...


class GameService:
    def __init__(self):
        self.__repository = Game.objects
        self.__players_games_repository = PlayersGames.objects
        self.__player_repository = Player.objects

    def get_week_games(self) -> WeekGames:
        previous_week_game: Game | None = (
            self.__repository.get_previous_week_game()
        )
        next_week_game: Game | None = self.__repository.get_next_week_game()
        return WeekGames(previous=previous_week_game, next=next_week_game)

    @transaction.atomic
    def create_week_game(self) -> Game:
        last_game = self.__repository.get_previous_week_game()
        if not last_game:
            game = self.__repository.create_previous_week_game()
            self.__add_all_monthly_players(game)
            return game

        next_game = self.__repository.get_next_week_game()
        if not next_game:
            game = self.__repository.create_next_week_game()
            self.__add_all_monthly_players(game)
            return game

        raise GameAlreadyExistsException

    def __add_all_monthly_players(self, game) -> None:
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
