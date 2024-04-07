from datetime import datetime
from django.utils import timezone


from uuid import uuid4
from players.models import Player, PlayerBills, PlayerVisits


class PlayerMixins:
    # TODO: search for library that fake name
    def create_player(
        self,
        name=f"{uuid4()}",
        surname="Test Surname",
        alias="Test Alias",
        phone_number="+552199231212",
        is_monthly_player=True,
        active=True,
    ) -> Player:
        return Player.objects.create(
            name=name,
            surname=surname,
            alias=alias,
            phone_number=phone_number,
            is_monthly_player=is_monthly_player,
            active=active,
        )

    def create_player_bill(
        self,
        player: Player | None = None,
        due_date: datetime = timezone.now(),
        payed_date: datetime = timezone.now(),
        payed_value: float = 0,
    ) -> PlayerBills:
        if not player:
            player = self.create_player()

        return PlayerBills.objects.create(
            due_date=due_date,
            payed_date=payed_date,
            payed_value=payed_value,
            player=player,
        )

    def create_player_visit(
        self,
        player: Player | None = None,
        visit_day: datetime = timezone.now(),
        payed_value: float = 0,
    ) -> PlayerVisits:
        if not player:
            player = self.create_player()

        return PlayerVisits.objects.create(
            visit_day=visit_day, payed_value=payed_value, player=player
        )

    def create_player_game(self, player): ...
