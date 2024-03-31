


from players.models import Player


class PlayerMixins:

    def create_player(
            self,
            name="Test Name",
            surname="Test Surname",
            alias="Test Alias",
            phone_number="+552199231212",
            is_monthly_player=True,
            active=True,
        ):
        return Player.objects.create(
            name=name,
            surname=surname,
            alias=alias,
            phone_number=phone_number,
            is_monthly_player=is_monthly_player,
            active=active
        )