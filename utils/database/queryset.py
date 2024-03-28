from django.db import models


class SoftDeleteQuerySet(models.QuerySet):
    def deleted(self):
        return self.filter(deleted=False)

class BaseQuerySet(SoftDeleteQuerySet): ...
