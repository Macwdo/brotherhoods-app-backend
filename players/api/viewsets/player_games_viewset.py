from players.api.serializers import PlayersGamesSerializer
from players.api.viewsets import PlayerRelationModelViewSet
from players.models import PlayersGames


class PlayersGamesViewSet(PlayerRelationModelViewSet):
    queryset = PlayersGames.objects.all()
    serializer_class = PlayersGamesSerializer
