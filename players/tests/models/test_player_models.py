from datetime import timedelta
from django.utils import timezone
from django.test import TestCase
import pytest
from players.tests.mixins.player_mixins import PlayerMixins


class PlayerModelTest(TestCase, PlayerMixins):
    def setUp(self):
        self.__player = self.create_player()

    @pytest.mark.model
    def test_player_model_str(self):
        assert (
            str(self.__player)
            == f"Player[id={self.__player.id}, name={self.__player.name}]"
        )

    @pytest.mark.model
    def test_player_model_repr(self):
        assert (
            repr(self.__player)
            == f"Player[id={self.__player.id}, name={self.__player.name}]"
        )


class PlayerVisitsModelTest(TestCase, PlayerMixins):
    def setUp(self):
        self.__player_visit = self.create_player_visit(payed_value=10)

    @pytest.mark.model
    def test_player_visit_payed_value(self):
        assert self.__player_visit.payed


class PlayerBillsModelTest(TestCase, PlayerMixins):
    def setUp(self):
        self.__player_bill = self.create_player_bill(payed_value=10)

    @pytest.mark.model
    def test_player_bill_payed_value(self):
        assert self.__player_bill.payed

    @pytest.mark.model
    def test_player_bill_is_overdue(self):
        self.__player_bill.due_date = timezone.now() + timedelta(days=1)
        self.__player_bill.payed_value = 0
        assert self.__player_bill.is_overdue

    @pytest.mark.model
    def test_player_bill_was_overdue_payment(self):
        self.__player_bill.due_date = timezone.now() - timedelta(days=1)
        self.__player_bill.payed_date = timezone.now()
        self.__player_bill.payed_value = 10
        assert self.__player_bill.was_overdue_payment
