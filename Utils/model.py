from datetime import datetime

from django.db import models


class SoftDeleteManager(models.Manager):
    def delete(self):
        return self.update(deleted_at=datetime.now().timestamp())

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at=0)


class ModelPlus(models.Model):
    deleted_at = models.FloatField(null=True, blank=True, default=0)
    objects = SoftDeleteManager()
    _objects = models.Manager()

    class Meta:
        default_manager_name = "objects"
        abstract = True
