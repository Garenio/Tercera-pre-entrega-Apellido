from django.contrib import admin
from guia_ciudad.models import Comercio, Restaurant, Propiedad, Clasificado

admin.site.register(Comercio)
admin.site.register(Restaurant)
admin.site.register(Propiedad)
admin.site.register(Clasificado)