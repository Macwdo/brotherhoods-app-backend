from __future__ import annotations

from django.db import models

from utils.models import BaseModel
from utils.time import (
    get_previous_wednesday_date,
    get_next_wednesday_date,
)


class GameManager(models.Manager):
    def create_previous_week_game(self):
        previous_wednesday = get_previous_wednesday_date()
        return self.create(game_day=previous_wednesday)

    def create_next_week_game(self):
        next_wednesday = get_next_wednesday_date()
        return self.create(game_day=next_wednesday)


class GameQuerySet(models.QuerySet):
    def get_month_games(self):
        next_wedsnesday = get_next_wednesday_date()
        return self.filter(
            game_day__month=next_wedsnesday.month,
            game_day__year=next_wedsnesday.year,
        )

    def get_last_game(self):
        previous_wednesday = get_previous_wednesday_date()
        return self.filter(
            game_day__day=previous_wednesday.day,
            game_day__month=previous_wednesday.month,
            game_day__year=previous_wednesday.year,
        )

    def get_next_game(self):
        next_wednesday = get_next_wednesday_date()
        return self.filter(
            game_day__day=next_wednesday.day,
            game_day__month=next_wednesday.month,
            game_day__year=next_wednesday.year,
        )


class Game(BaseModel):
    game_day = models.DateTimeField()

    objects = GameManager.from_queryset(GameQuerySet)()
