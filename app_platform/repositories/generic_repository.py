from abc import ABC, abstractmethod




class IGenericRepository(ABC):

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self):
        pass

    @abstractmethod
    def get_filter(self, **kwargs):
        pass

    @abstractmethod
    def get_fields_only(self, **kwargs):
        pass

