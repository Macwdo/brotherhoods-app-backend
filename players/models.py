from __future__ import annotations, absolute_import

from utils.database.manager import BaseManager
from utils.database.models import BaseModel
from django.db import models
from django.utils import timezone

from utils.database.queryset import BaseQuerySet


class PlayerManager(BaseManager): ...


class PlayerQuerySet(BaseQuerySet):
    def get_monthly_players(self) -> PlayerQuerySet:
        return self.filter(is_monthly_player=True)

    def get_active_players(self) -> PlayerQuerySet:
        return self.filter(active=True)
    
    def search_players_by_string_fields(self, search_term: str) -> PlayerQuerySet:
        return self.filter(
            models.Q(name__istartswith=search_term)
            | models.Q(surname__istartswith=search_term)
            | models.Q(alias__istartswith=search_term)
            | models.Q(phone_number__istartswith=search_term)
            | models.Q(email__istartswith=search_term)
        )


class Player(BaseModel):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50, blank=True, null=True)
    alias = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    is_monthly_player = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    birth_date = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    objects = PlayerManager.from_queryset(PlayerQuerySet)()

    def __str__(self) -> str:
        return f"Player[id={self.id}, name={self.name}]"

    def __repr__(self) -> str:
        return f"Player[id={self.id}, name={self.name}]"


class PlayerVisits(BaseModel):
    visit_day = models.DateTimeField()
    payed_value = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    player = models.ForeignKey(
        "Player", related_name="visits", on_delete=models.CASCADE
    )

    @property
    def payed(self) -> bool:
        return self.payed_value > 0


class PlayerBills(BaseModel):
    due_date = models.DateTimeField()
    payed_date = models.DateTimeField(blank=True, null=True)
    payed_value = models.DecimalField(
        max_digits=5, decimal_places=2, blank=False
    )

    player = models.ForeignKey(
        "Player", related_name="bills", on_delete=models.PROTECT
    )

    @property
    def payed(self) -> bool:
        return self.payed_value > 0

    @property
    def is_overdue(self):
        return not self.payed and self.due_date > timezone.now()

    @property
    def was_overdue_payment(self):
        return self.payed and self.payed_date > self.due_date


class PlayersGames(BaseModel):
    as_monthly_player = models.BooleanField(default=False)

    game = models.ForeignKey(
        "games.Game", related_name="games", on_delete=models.PROTECT
    )
    player = models.ForeignKey(
        "Player", related_name="games", on_delete=models.PROTECT
    )
