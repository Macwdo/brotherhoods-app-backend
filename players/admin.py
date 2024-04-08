# Register your models here.
from django.contrib import admin

from players.models import Player, PlayerVisits, PlayerBills, PlayersGames

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "alias", "phone_number", "is_monthly_player", "active", "birth_date", "email")
    search_fields = ("name", "surname", "alias", "phone_number", "email")
    list_filter = ("is_monthly_player", "active")
    list_editable = ("is_monthly_player", "active")
    list_per_page = 20

@admin.register(PlayerVisits)
class PlayerVisitsAdmin(admin.ModelAdmin):
    list_display = ("visit_day", "payed_value", "player")
    search_fields = ("visit_day", "payed_value", "player")
    list_filter = ("visit_day", "payed_value")
    list_editable = ("payed_value",)
    list_per_page = 20


@admin.register(PlayerBills)
class PlayerBillsAdmin(admin.ModelAdmin):
    list_display = ("due_date", "payed_date", "payed_value", "player")
    search_fields = ("due_date", "payed_date", "payed_value", "player")
    list_filter = ("due_date", "payed_date", "payed_value")
    list_editable = ("payed_date", "payed_value")
    list_per_page = 20


@admin.register(PlayersGames)
class PlayersGamesAdmin(admin.ModelAdmin):
    pass