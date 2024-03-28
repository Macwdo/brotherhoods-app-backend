from __future__ import annotations

from utils.models import BaseModel
from django.db import models


class PlayerManager(models.Manager): ...


class PlayerQuerySet(models.QuerySet):
    def get_monthly_players(self):
        return self.filter(is_monthly_player=True)

    def get_active_players(self):
        return self.filter(active=True)


class Player(BaseModel):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50, blank=True, null=True)
    alias = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    is_monthly_player = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    objects = PlayerManager.from_queryset(PlayerQuerySet)()


class PlayerVisits(BaseModel):
    player = models.ForeignKey(
        "Player", related_name="visits", on_delete=models.CASCADE
    )
    visit_day = models.DateTimeField()
    payed_value = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    @property
    def payed(self):
        return self.payed_value > 0


class PlayerBill(BaseModel):
    due_date = models.DateTimeField()
    payed_date = models.DateTimeField()
    payed_value = models.DecimalField(
        max_digits=5, decimal_places=2, blank=False
    )

    player = models.ForeignKey(
        "Player", related_name="bills", on_delete=models.PROTECT
    )


class PlayersGames(BaseModel):
    as_monthly_player = models.BooleanField(default=False)

    game = models.ForeignKey(
        "games.Game", related_name="games", on_delete=models.PROTECT
    )
    player = models.ForeignKey(
        "Player", related_name="games", on_delete=models.PROTECT
    )
