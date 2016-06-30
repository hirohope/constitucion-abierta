from django.contrib import admin

# Register your models here.

from constitucion import models 

admin.site.register(models.Acta)
admin.site.register(models.RoundRobin)
