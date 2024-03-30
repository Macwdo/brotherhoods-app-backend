from django.db import models

from utils.database.soft_delete import SoftDeleteModel


class TimeStampModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModelMixins(TimeStampModelMixin, SoftDeleteModel):
    class Meta:
        abstract = True


class BaseModel(BaseModelMixins):
    class Meta:
        abstract = True