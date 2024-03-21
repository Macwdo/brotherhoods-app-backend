from abc import ABC, abstractmethod
from app_platform.models import Game as GameModel


class IGameService(ABC):

    @abstractmethod
    def create_game_day(self) -> GameModel:
        pass

    @abstractmethod
    def get_month_games(self) -> list[GameModel]:
        pass


class GameService(IGameService):
    def __init__(self):
        self.__game_repository =