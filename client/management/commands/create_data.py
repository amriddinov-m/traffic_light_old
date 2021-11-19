import datetime

from django.core.management.base import BaseCommand

from client.models import Client
from department.models import Department
from entity.models import Entity


class Command(BaseCommand):
    help = 'Initialize base data for test'

    def handle(self, *args, **options):
        for i in range(0, 200):
            Entity.objects.create(
                updated_at=datetime.datetime.now(),
                full_name='FullName Test #' + str(i),
                short_name='ShortName Test #' + str(i),
                inn='123456789' + str(i),
                kpp='987654321' + str(i)
            )
        for i in range(0, 500):
            Department.objects.create(
                title='Title Test #' + str(i),
            )
        for i in range(0, 3000):
            Client.objects.create(
                phone='+99899032340' + str(i),
                first_name='FirstName Test #' + str(i),
                surname='SurName Test #' + str(i),
                patronymic='Patronymic Test #' + str(i),
                _type='primary',
                sex='male',
                ok='ok@' + str(i),
                instagram='instagram@' + str(i),
                telegram='telegram@' + str(i),
                whatsapp='whatsapp@' + str(i),
                viber='viber@' + str(i),
            )
