from players.models import Player


class PlayerService:
    def __init__(self):
        self.__repository = Player.objects
