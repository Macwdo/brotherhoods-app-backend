from django.db import models


class BaseModel:
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Player(models.Model, BaseModel):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50, blank=True, null=True)
    alias = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    is_monthly_player = models.BooleanField(default=False)
    active = models.BooleanField(default=True)


class PlayerBill(models.Model, BaseModel):
    due_date = models.DateTimeField()
    payed_date = models.DateTimeField()
    payed_value = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    player = models.ForeignKey(Player, related_name="bills", on_delete=models.PROTECT)


class Game(models.Model, BaseModel):
    game_day = models.DateTimeField()


class PlayersGames(models.Model, BaseModel):
    as_monthly_player = models.BooleanField(default=False)

    game = models.ForeignKey(Game, related_name="games", on_delete=models.PROTECT)
    player = models.ForeignKey(Player, related_name="games", on_delete=models.PROTECT)
