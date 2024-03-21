from abc import ABC, abstractmethod
from app_platform.models import Game as GameModel, PlayersGames

from app_platform.services.player_service import PlayerService
from app_platform.utils import get_next_wednesday_date


class IGameService(ABC):
    @abstractmethod
    def create_game_day(self):
        pass

    @abstractmethod
    def get_month_games(self):
        pass


class GameService(IGameService):
    def __init__(self):
        self.__repository = GameModel.objects
        self.__players_games_repository = PlayersGames.objects
        self.__player_service = PlayerService()

    def get_month_games(self):
        pass

    def create_game_day(self):
        next_wednesday_date = get_next_wednesday_date()
        game = self.__repository.create(game_day=next_wednesday_date)
        self.__add_all_monthly_players(game)

    def __add_all_monthly_players(self, game):
        monthly_players = self.__player_service.get_monthly_players().values(
            "id", "is_monthly_player"
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
