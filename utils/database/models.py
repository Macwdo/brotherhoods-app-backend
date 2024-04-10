from utils.database.base_models.time_stamp import TimeStampModelMixin

from utils.database.base_models.soft_delete import SoftDeleteModel
from utils.database.manager import BaseManager
from utils.database.queryset import BaseQuerySet


class BaseModelMixins(TimeStampModelMixin, SoftDeleteModel):
    class Meta:
        abstract = True


class BaseModel(BaseModelMixins):
    def delete(self, using=None, keep_parents=False):
        self.soft_delete()

    class Meta:
        abstract = True
