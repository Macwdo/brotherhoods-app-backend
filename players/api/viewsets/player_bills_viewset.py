from players.api.serializers import PlayerBillSerializer
from players.api.viewsets import PlayerRelationModelViewSet
from players.models import PlayerBills


class PlayerBillViewSet(PlayerRelationModelViewSet):
    queryset = PlayerBills.objects.all()
    serializer_class = PlayerBillSerializer