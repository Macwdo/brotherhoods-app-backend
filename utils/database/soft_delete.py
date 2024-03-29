from django.db import models
from django.utils import timezone


class SoftDeleteQuerySet(models.QuerySet):
    def deleted(self):
        return self.filter(deleted=False)


class SoftDeleteManager(models.Manager): ...


class SoftDeleteModelMixin(models.Model):
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, default=None)

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.deleted = True
        self.save()

    def restore(self):
        self.deleted_at = None
        self.deleted = False
        self.save()

    class Meta:
        abstract = True
