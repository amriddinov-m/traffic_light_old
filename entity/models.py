from django.db import models


class Entity(models.Model):
    entity_id = models.BigIntegerField(verbose_name='Идентификатор (01)', editable=False,
                                       blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    full_name = models.CharField(max_length=255,
                                 verbose_name='Полное название')
    short_name = models.CharField(max_length=255,
                                  verbose_name='Сокращенное название',
                                  blank=True, null=True)
    inn = models.CharField(max_length=255,
                           verbose_name='ИНН')
    kpp = models.CharField(max_length=255,
                           verbose_name='КПП')

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        super(Entity, self).save(*args, **kwargs)
        if self.id:
            entity_id = int(str(self.id) + '02')
            Entity.objects.filter(id=self.id).update(entity_id=entity_id)

    class Meta:
        verbose_name = 'Юр.Лицо'
        verbose_name_plural = 'Юр.Лица'
