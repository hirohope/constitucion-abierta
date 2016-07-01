from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from random import randint

# Create your models here.


def assign_robin(sender, instance, created, **kwargs):
    if created and instance.responsible == '':
        n = Acta.objects.count()
        robin = RoundRobin.get_one(n)
        instance.responsible = robin.name
        instance.save()

class Acta(models.Model):
    
    name = models.CharField(max_length=128)

    static = models.CharField(max_length=128)
    secret = models.CharField(max_length=128)
    valid = models.BooleanField(default=False)
    sheet_row = models.IntegerField(default=0)
    notified = models.BooleanField(default=False)
    comuna = models.CharField(max_length=128, default='')
    date = models.DateField(null=True, blank=True)
    person_name = models.CharField(max_length=128, default='')
    responsible = models.CharField(max_length=128, default='')

    def __str__(self):

        return "id %s - hash %s - valid %s - notified %s - responsible %s" % (
            self.id, self.name, self.valid, self.notified, self.responsible
        )

    def get_all_valid():
        actas = Acta.objects.filter(valid = True)
        return actas

    def get_direct_url(self):
        acta_url = settings.TEMPLATE_DIRECT_ACTA_URL % self.static
        return acta_url

    def get_url(self):
        acta_url = settings.TEMPLATE_ACTA_URL % self.static
        return acta_url

    def get_modify_url(self):
        acta_modificar_url = settings.TEMPLATE_ACTA_MODIFICAR_URL % (self.static, self.secret)
        return acta_modificar_url

    def get_thumbnail_url(self):
        url = settings.TEMPLATE_THUMBNAIL % self.name
        return url

    def get_thumbnail_path(self):
        path = settings.TEMPLATE_THUMBNAIL_STATIC % self.name
        return path

    @staticmethod
    def get_random():
        count = Acta.objects.count()
        random_index = randint(0, count - 1)
        return Acta.objects.all()[random_index]


models.signals.post_save.connect(assign_robin, sender=Acta)


class RoundRobin(models.Model):
    
    name = models.CharField(max_length=128)
    mail = models.EmailField()
    
    @staticmethod
    def get_one(index):
        n = RoundRobin.objects.count()
        selected = RoundRobin.objects.all().order_by('id')[index%n]

        return selected

