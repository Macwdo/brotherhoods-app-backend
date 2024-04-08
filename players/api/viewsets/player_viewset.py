from django.db.models.query import QuerySet
from players.api.serializers import PlayerSerializer
from players.models import Player
from project.api.viewsets.base_viewsets import BaseModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend



class PlayerRelationModelViewSet(BaseModelViewSet):
    def get_queryset(self):        
        return super().get_queryset().filter(player_id=self.kwargs["player_pk"])

    def perform_create(self, serializer):
        serializer.save(player_id=self.kwargs["player_pk"])


class PlayerViewSet(BaseModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = [
        "name",
        "surname",
        "email",
        "phone_number"
    ]

    def filter_queryset(self, queryset: QuerySet) -> QuerySet:
        result = super().filter_queryset(queryset)
        return result
