from utils.database.base_models.time_stamp import TimeStampModelMixin

from utils.database.base_models.soft_delete import SoftDeleteModel


class BaseModelMixins(TimeStampModelMixin, SoftDeleteModel):
    class Meta:
        abstract = True


class BaseModel(BaseModelMixins):
    class Meta:
        abstract = True
