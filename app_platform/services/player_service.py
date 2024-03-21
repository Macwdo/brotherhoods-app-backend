from abc import ABC, abstractmethod
from app_platform.models import Player


class IPlayerService(ABC):
    @abstractmethod
    def get_monthly_players(self):
        pass


class PlayerService(IPlayerService):
    def __init__(self):
        self.__repository = Player.objects

    def get_monthly_players(self):
        return self.__repository.filter(is_monthly_player=True)
