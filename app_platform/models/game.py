from __future__ import annotations

from datetime import datetime

from app_platform.models.base import BaseModel
from django.db import models



class GameManager(models.Manager): ...


class GameQuerySet(models.QuerySet):

    def get_month_games(self):
        today = datetime.today()
        return self.filter(
            game_day__month=today.month,
            game_day__year=today.year
        )


class Game(BaseModel):
    game_day = models.DateTimeField()
