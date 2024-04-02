from __future__ import annotations
from django.db import models
from django.utils import timezone


class SoftDeleteModel(models.Model):
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, default=None)

    def soft_delete(self) -> SoftDeleteModel:
        self.deleted_at = timezone.now()
        self.deleted = True
        self.save()
        return self

    def restore(self) -> SoftDeleteModel:
        self.deleted_at = None
        self.deleted = False
        self.save()
        return self

    class Meta:
        abstract = True


class SoftDeleteQuerySet(models.QuerySet[SoftDeleteModel]):
    def deleted(self) -> models.QuerySet[SoftDeleteModel]:
        return self.filter(deleted=True)


class SoftDeleteManager(models.Manager[SoftDeleteModel]): ...
