from django.urls import path

from guia_ciudad.views import (
    agregar_comercio, buscar_comercios, agregar_restaurant, buscar_restaurantes,
    agregar_propiedad, buscar_propiedades, agregar_clasificado, buscar_clasificados, 
)


urlpatterns = [
    path('agregar-comercio/', agregar_comercio, name="agregar_comercio"),
    path('buscar-comercios/', buscar_comercios, name="buscar_comercios"),
    path('agregar-restaurant/', agregar_restaurant, name="agregar_restaurant"),
    path('buscar-restaurantes/', buscar_restaurantes, name="buscar_restaurantes"),
    path('agregar-propiedad/', agregar_propiedad, name="agregar_propiedad"),
    path('buscar-propiedades/', buscar_propiedades, name="buscar_propiedades"),
    path('agregar-clasificado/', agregar_clasificado, name="agregar_clasificado"),
    path('buscar-clasificados/', buscar_clasificados, name="buscar_clasificados"),   
]