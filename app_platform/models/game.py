from app_platform.models.base import BaseModel
from django.db import models


class Game(BaseModel):
    game_day = models.DateTimeField()
