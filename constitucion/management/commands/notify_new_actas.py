# -*- coding: UTF-8 -*-.
import os
import datetime
import constitucion.spreadsheet as sp
import constitucion.myemail as email

from constitucion.models import Acta, RoundRobin
from django.conf import settings

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        def notify_new_actas():
            with open(settings.CRONLOG, 'a') as fp:
                acta = Acta.objects.filter(notified = False).first()
                while acta is not None:
                    n = Acta.objects.filter(notified = True).count()
                    sp.insert(n+2, acta.id, acta.get_direct_url(), acta.get_modify_url(), acta.responsible)
                    robin = RoundRobin.objects.filter(name=acta.responsible).first()
                    acta.sheet_row = n+2
                    acta.save()
                    email.send_email(
                        settings.EMAIL,
                        robin.mail,
                        robin.name,
                        acta.id,
                        acta.get_direct_url(),
                        acta.get_modify_url()
                    )
                    fp.write('[%s] send email to %s - acta %s\n' % (datetime.datetime.now(), robin.mail, acta.id))
                    acta.notified = True
                    acta.save()
                    acta = Acta.objects.filter(notified = False).first()

        with open(settings.CRONLOG, 'a') as fp:
            fp.write('starting %s\n' % datetime.datetime.now())
            notify_new_actas()
            fp.write('finishing %s\n' % datetime.datetime.now())
