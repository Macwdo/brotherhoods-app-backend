from rest_framework_nested.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from games.api.viewsets import GameViewSet
from players.api.viewsets import PlayersGamesViewSet

game_router = SimpleRouter()
game_router.register(r"games", viewset=GameViewSet)

nested_games_router = NestedSimpleRouter(game_router, "games", lookup="game")
nested_games_router.register(
    "players", viewset=PlayersGamesViewSet, basename="game-players"
)
