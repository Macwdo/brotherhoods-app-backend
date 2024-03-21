import logging
from abc import ABC, abstractmethod
from django.db.models import Model, QuerySet
from django.core.exceptions import FieldError

# https://docs.djangoproject.com/en/5.0/howto/logging/#using-logger-hierarchies-and-propagation
logger = logging.getLogger(__name__)


class IGenericRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, id: int):
        pass

    @abstractmethod
    def get_by_filter(self, **fields):
        pass

    @abstractmethod
    def get_fields_only(self, id: int, **fields):
        pass

    @abstractmethod
    def update(self, id: int, **fields):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass


class GenericRepository(IGenericRepository):
    def __init__(self, model: Model):
        if not model:
            raise Exception("To use generic repository you must to define self._model")
        self._model = model

    def get_all(self) -> QuerySet[Model]:
        return self._model.objects.all()

    def get_by_id(self, id: int) -> Model | None:
        try:
            object = self._model.objects.get(id=id)
            return object
        except self._model.DoesNotExist:
            logger.warning(f"Error trying to get model {self.__model} by id {id}")
        return None

    def get_by_filter(self, **fields) -> QuerySet[Model]:
        import ipdb; ipdb.set_trace()
        query = self._model.objects.filter(**fields)
        return query

    def get_fields_only(self, id: int, **fields):
        pass

    def update(self, id: int, **fields):
        try:
            object = self.get_by_filter(**fields)
            if object:
                object.update(**fields)
                return object
        except FieldError as e:
            logger.error("Error trying to update model: Invalid Field.")
            raise e
        except Exception as e:
            logger.error(f"Error trying to update model: {repr(e)}")

    def delete(self, id: int) -> None:
        object = self.get_by_id(id)
        if object:
            object.delete()
