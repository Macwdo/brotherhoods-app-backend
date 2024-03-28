from django.db import models
from django.utils import timezone


class TimeStampModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


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


class BaseModelMixins(TimeStampModelMixin, SoftDeleteModelMixin):
    class Meta:
        abstract = True


class BaseModel(BaseModelMixins):
    class Meta:
        abstract = True
