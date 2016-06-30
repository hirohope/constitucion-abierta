# -*- coding: UTF-8 -*-.

#(nombre, mail)
from django.conf import settings


if settings.LOCAL:
    roundrobin = [
        ("Constitucion Abierta 1", "camilogarridogarcia@gmail.com"),
    ]
else:
    roundrobin = [
        ("Sebastián Ferrada", "scferradaa@gmail.com"),
        ("Jorge Pérez", "jorgeperezrojas@gmail.com"),
        ("Claudio Gutiérrez", "cgutierr@dcc.uchile.cl"),
        ("Juan Reutter", "juan.reutter@gmail.com"),
        ("Adrian Soto", "assoto@uc.cl"),
        ("Lucas Cabello", "lmcabellog@gmail.com"),
        ("Mauricio Quezada", "waxkun@gmail.com"),
    ]
