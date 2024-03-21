from datetime import datetime
from abc import ABC, abstractmethod
from app_platform.models import Game
from app_platform.repositories.generic_repository import GenericRepository


class IGameRepository(ABC):
    @abstractmethod
    def get_current_month_games(self):
        pass


class GameRepository(IGameRepository):
    def __init__(self):
        self.__generic_repository = GenericRepository(Game)

    def get_current_month_games(self):
        today = datetime.today()
        return self.__generic_repository.get_by_filter(
            game_day__month=today.month,
            game_day__year=today.year
        )
