from django import forms


class ComercioFormulario(forms.Form):
    nombre = forms.CharField(max_length=128)
    categoria = forms.CharField(max_length=128)
    direccion = forms.CharField(max_length=128)
    horario = forms.CharField(max_length=128)

class RestaurantFormulario(forms.Form):
    nombre = forms.CharField(max_length=128)
    especialidad = forms.CharField(max_length=128)
    direccion = forms.CharField(max_length=128)
    horario = forms.CharField(max_length=128)

class PropiedadFormulario(forms.Form):
    tipo = forms.CharField(max_length=128)
    operacion = forms.CharField(max_length=128)
    habitaciones = forms.IntegerField()
    precio = forms.IntegerField()
    contacto = forms.EmailField()

class ClasificadoFormulario(forms.Form):
    producto = forms.CharField(max_length=128)
    descripcion = forms.CharField(max_length=256)
    precio = forms.IntegerField()
    contacto = forms.EmailField()