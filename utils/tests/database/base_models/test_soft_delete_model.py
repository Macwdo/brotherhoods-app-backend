from __future__ import annotations

import pytest
from django.test import TestCase

from players.tests.mixins.player_mixins import PlayerMixins


class SoftDeleteModelTest(TestCase, PlayerMixins):
    def setUp(self):
        self.__some_soft_delete_model = self.create_player()

    @pytest.mark.model
    def test_soft_delete(self):
        model = self.__some_soft_delete_model
        model.soft_delete()
        assert model.deleted

    @pytest.mark.model
    def test_restore(self):
        model = self.__some_soft_delete_model
        model.soft_delete()

        assert model.deleted
        model.restore()

        assert not model.deleted


class SoftDeleteQuerySetTest(TestCase, PlayerMixins):
    def setUp(self):
        self.__some_soft_delete_model = self.create_player()

    @pytest.mark.model
    def test_query_soft_deleted_models(self):
        model = self.__some_soft_delete_model._meta.model
        player_0 = self.__some_soft_delete_model
        player_0.soft_delete()
        self.create_player()

        assert model.objects.deleted().count() == 1
        assert model.objects.deleted().first() == player_0
