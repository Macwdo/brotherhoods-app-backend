from players.api.routes import player_router, nested_player_router

app_name = "players"
urlpatterns = []
urlpatterns += player_router.urls
urlpatterns += nested_player_router.urls
