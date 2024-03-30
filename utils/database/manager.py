from utils.database.soft_delete import SoftDeleteManager


class BaseManagerMixins(SoftDeleteManager): ...


class BaseManager(BaseManagerMixins): ...
