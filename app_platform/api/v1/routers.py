from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from app_platform.api.v1.viewsets import PlayerViewSet, PlayerBillViewSet, GameViewSet, PlayersGamesViewSet

player_router = SimpleRouter()
player_router.register(r"players", viewset=PlayerViewSet)

nested_player_router = NestedSimpleRouter(player_router, "players")
nested_player_router.register("bills", viewset=PlayerBillViewSet)
nested_player_router.register("games", viewset=PlayersGamesViewSet)

game_router = SimpleRouter()
game_router.register(r"games", viewset=GameViewSet)

nested_games_router = NestedSimpleRouter(game_router, "games")
nested_games_router.register("players", viewset=PlayersGamesViewSet)


v1_router = SimpleRouter()