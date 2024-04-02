from utils.database.base_models.soft_delete import SoftDeleteManager


class BaseManagerMixins(SoftDeleteManager): ...


class BaseManager(BaseManagerMixins): ...
