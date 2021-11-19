from django.db import models
import pytz

from department.models import Department
from entity.models import Entity


class Client(models.Model):
    class Status(models.TextChoices):
        active = 'active', 'Активный'
        deactive = 'deactive', 'Не активный'

    class Type(models.TextChoices):
        primary = 'primary', 'Первичный'
        repeated = 'repeated', 'Повторный'
        external = 'external', 'Внешний'
        indirect = 'indirect', 'Косвенный'

    class Sex(models.TextChoices):
        male = 'male', 'Мужской'
        female = 'female', 'Женский'
        another = 'another', 'Другой'

    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    client_id = models.BigIntegerField(verbose_name='Идентификатор (01)', editable=False,
                                       blank=True, null=True)
    entity = models.ForeignKey(Entity,
                               on_delete=models.PROTECT,
                               verbose_name='Юр.Лицо',
                               blank=True, null=True)
    department = models.ManyToManyField(Department, related_name='clients',
                                        verbose_name='Департамент',
                                        blank=True)
    phone = models.CharField(max_length=20,
                             verbose_name='Номер телефона',
                             unique=True)
    first_name = models.CharField(max_length=255,
                                  verbose_name='Имя')
    surname = models.CharField(max_length=255,
                               verbose_name='Фамилия',
                               blank=True, null=True)
    patronymic = models.CharField(max_length=255,
                                  verbose_name='Отчество',
                                  blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления',
                                      auto_now=True)
    status_updated_at = models.DateTimeField(verbose_name='Дата обновления статуса',
                                             auto_now=True)
    status = models.CharField(max_length=255,
                              verbose_name='Статус',
                              choices=Status.choices,
                              default='active')
    _type = models.CharField(max_length=255,
                             verbose_name='Тип',
                             choices=Type.choices)
    sex = models.CharField(max_length=255,
                           verbose_name='Пол',
                           choices=Sex.choices)
    timezone = models.CharField(max_length=32,
                                choices=TIMEZONES,
                                default='UTC')
    ok = models.CharField(max_length=255,
                          verbose_name='Одноклассники',
                          blank=True, null=True)
    instagram = models.CharField(max_length=255,
                                 verbose_name='Инстаграм',
                                 blank=True, null=True)
    telegram = models.CharField(max_length=255,
                                verbose_name='Телеграм',
                                blank=True, null=True)
    whatsapp = models.CharField(max_length=255,
                                verbose_name='Ватсапп',
                                blank=True, null=True)
    viber = models.CharField(max_length=255,
                             verbose_name='Вайбер',
                             blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} ({self.phone})'

    def save(self, *args, **kwargs):
        super(Client, self).save(*args, **kwargs)
        if self.id:
            client_id = int(str(self.id) + '01')
            Client.objects.filter(id=self.id).update(client_id=client_id)

    def get_full_name(self):
        return f'{self.surname} {self.first_name} {self.patronymic}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class ClientExtraPhone(models.Model):
    phone = models.CharField(max_length=255,
                             verbose_name='Номер телефона')
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE,
                               verbose_name='Клиент')

    def __str__(self):
        return f'{self.client.first_name} | {self.phone}'

    class Meta:
        verbose_name = 'Дополнительный номер клиента'
        verbose_name_plural = 'Дополнительные номера клиентов'


class ClientEmail(models.Model):
    email = models.EmailField(verbose_name='Почта', unique=False)
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE,
                               verbose_name='Клиент')

    def __str__(self):
        return f'{self.client.first_name} | {self.email}'

    class Meta:
        verbose_name = 'Email клиента'
        verbose_name_plural = 'Email клиентов'


class VK(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name='Название аккаунта')
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE,
                               verbose_name='Клиент')

    def __str__(self):
        return f'{self.client.first_name} | {self.title}'

    class Meta:
        verbose_name = 'VK аккаунт клиента'
        verbose_name_plural = 'VK аккаунты клиентов'


class FB(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name='Название аккаунта')
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE,
                               verbose_name='Клиент')

    def __str__(self):
        return f'{self.client.first_name} | {self.title}'

    class Meta:
        verbose_name = 'FB аккаунт клиента'
        verbose_name_plural = 'FB аккаунты клиентов'


class ClientAddedToDepartmentDate(models.Model):
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE,
                               verbose_name='Клиент')
    department = models.ForeignKey(Department,
                                   on_delete=models.CASCADE,
                                   verbose_name='Департамент')
    added_date = models.DateField(verbose_name='Дата добавления')

    def __str__(self):
        return f'{self.department} | {self.added_date}'

    class Meta:
        verbose_name = 'Дата добавления клиента'
        verbose_name_plural = 'Даты добавления клиентов'
