from games.api.routes import game_router, nested_games_router

app_name = "games"
urlpatterns = []
urlpatterns += game_router.urls
urlpatterns += nested_games_router.urls
