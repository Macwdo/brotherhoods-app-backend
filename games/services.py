from django.db import transaction
from games.models import Game
from games.types import WeekGames
from players.models import Player, PlayersGames


class GameAlreadyExistsException(Exception): ...


class GameService:
    def get_week_games(self) -> WeekGames:
        previous_week_game: Game | None = Game.objects.get_previous_week_game()
        next_week_game: Game | None = Game.objects.get_next_week_game()
        return WeekGames(previous=previous_week_game, next=next_week_game)

    @transaction.atomic
    #TODO: Create service tests and test logic with freezed time
    def create_week_game(self) -> Game:
        last_game = Game.objects.get_previous_week_game()
        if not last_game:
            game = Game.objects.create_previous_week_game()
            self.__add_all_monthly_players(game)
            return game

        next_game = Game.objects.get_next_week_game()
        if not next_game:
            game = Game.objects.create_next_week_game()
            self.__add_all_monthly_players(game)
            return game

        raise GameAlreadyExistsException

    def __add_all_monthly_players(self, game) -> None:
        monthly_players = (
            Player.objects.get_monthly_players()
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
        PlayersGames.objects.bulk_create(players_games_instances)
