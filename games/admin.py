from django.contrib import admin
from games.models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin): ...
