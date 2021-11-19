from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from entity.models import Entity


class Department(MPTTModel):
    department_id = models.BigIntegerField(verbose_name='Идентификатор (03)', editable=False,
                                           blank=True, null=True)
    title = models.CharField(max_length=255,
                             verbose_name='Название')
    entity = models.ForeignKey(Entity,
                               on_delete=models.PROTECT,
                               verbose_name='Юр.Лицо',
                               blank=True, null=True)
    parent = TreeForeignKey('self',
                            on_delete=models.CASCADE,
                            null=True, blank=True,
                            related_name='children')

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Department, self).save(*args, **kwargs)
        if self.id:
            department_id = int(str(self.id) + '03')
            Department.objects.filter(id=self.id).update(department_id=department_id)

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'
