from __future__ import annotations
from time import strftime

from django.db import models

from utils.database.manager import BaseManager
from utils.database.models import BaseModel
from utils.database.queryset import BaseQuerySet
from utils.time import (
    get_previous_wednesday_date,
    get_next_wednesday_date,
)


class GameManager(BaseManager):
    def create_previous_week_game(self):
        previous_wednesday = get_previous_wednesday_date()
        return self.create(game_day=previous_wednesday)

    def create_next_week_game(self) -> Game:
        next_wednesday = get_next_wednesday_date()
        return self.create(game_day=next_wednesday)
    
    
    def get_previous_week_game(self) -> Game | None:
        try:
            previous_wednesday = get_previous_wednesday_date()
            return self.get(
                game_day__day=previous_wednesday.day,
                game_day__month=previous_wednesday.month,
                game_day__year=previous_wednesday.year,
            )
        except self.model.DoesNotExist:
            return None

    def get_next_week_game(self) -> Game | None:
        try: 
            next_wednesday = get_next_wednesday_date()
            return self.get(
                game_day__day=next_wednesday.day,
                game_day__month=next_wednesday.month,
                game_day__year=next_wednesday.year,
            )
        except self.model.DoesNotExist:
            return None

class GameQuerySet(BaseQuerySet):
    def get_month_games(self) -> GameQuerySet:
        next_wedsnesday = get_next_wednesday_date()
        return self.filter(
            game_day__month=next_wedsnesday.month,
            game_day__year=next_wedsnesday.year,
        )


class Game(BaseModel):
    game_day = models.DateTimeField()

    objects = GameManager.from_queryset(GameQuerySet)()

    def __str__(self) -> str:
        return f"Game[id={self.id}, game_day={self.game_day.strftime('%d/%m/%Y')}]"
    
    def __repr__(self) -> str:
        return f"Game[id={self.id}, game_day={self.game_day.strftime('%d/%m/%Y')}]"