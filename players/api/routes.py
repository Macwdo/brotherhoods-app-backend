from rest_framework_nested.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from players.api.viewsets import (
    PlayerViewSet,
    PlayerBillViewSet,
    PlayersGamesViewSet,
)

player_router = SimpleRouter()
player_router.register(r"players", viewset=PlayerViewSet)

nested_player_router = NestedSimpleRouter(
    player_router, "players", lookup="player"
)
nested_player_router.register(
    "bills", viewset=PlayerBillViewSet, basename="player-bills"
)
nested_player_router.register(
    "games", viewset=PlayersGamesViewSet, basename="player-games"
)
