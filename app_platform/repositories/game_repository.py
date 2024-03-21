from abc import ABC, abstractmethod
from app_platform.models import Game as GameModel


class IGameRepository(ABC):

    @abstractmethod
    def create_game(self) -> GameModel:
        pass

    @abstractmethod
    def get_last_month_games(self) -> list[GameModel]:
        pass

    @
    def


class GameRepository(IGameRepository):
    def __init__(self):
        self.__game_repository =