from django.urls import path, include
from app_platform.api.v1.routers import (
    nested_player_router,
    player_router,
    game_router,
    nested_games_router,
)

app_name = "app_platform"

api_v1 = []
api_v1 += nested_player_router.urls
api_v1 += player_router.urls
api_v1 += game_router.urls
api_v1 += nested_games_router.urls

urlpatterns = [
    path(r"", include(api_v1))
]
