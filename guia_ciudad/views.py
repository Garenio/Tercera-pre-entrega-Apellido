from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from guia_ciudad.models import Comercio, Restaurant, Propiedad, Clasificado
from guia_ciudad.forms import ComercioFormulario, RestaurantFormulario, PropiedadFormulario, ClasificadoFormulario

## VIEW PÁGINA DE INICIO
def inicio(request):
    return render(
        request=request,
        template_name='guia_ciudad/inicio.html',
    )

## VIEWS PÁGINAS DE COMERCIOS
def listar_comercios(request):
    contexto = {
        'comercios': Comercio.objects.all()
    }
    return render(
        request=request,
        template_name='guia_ciudad/comercios.html',
        context=contexto,
    )

def agregar_comercio(request):
    if request.method == "POST":
        formulario = ComercioFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            comercio = Comercio(
                nombre=data['nombre'],
                categoria=data['categoria'],
                direccion=data['direccion'],
                horario=data['horario'],
                )
            comercio.save()
            url_exitosa = reverse('listar_comercios')
            return redirect(url_exitosa)
    else:  # GET
        formulario = ComercioFormulario()
    return render(
        request=request,
        template_name='guia_ciudad/formulario_comercio.html',
        context={'formulario': formulario},
    )

def buscar_comercios(request):
    if request.method == "POST":
        data = request.POST
        comercios = Comercio.objects.filter(
            Q(nombre__contains=data['busqueda']) | Q(categoria__contains=data['busqueda'])
        )
        contexto = {
            'comercios': comercios
        }
        return render(
            request=request,
            template_name='guia_ciudad/comercios.html',
            context=contexto,
        )

## VIEWS PÁGINAS DE GASTRONOMÍA
def listar_restaurantes(request):
    contexto = {
        'restaurantes': Restaurant.objects.all()
    }
    return render(
        request=request,
        template_name='guia_ciudad/restaurantes.html',
        context=contexto,
    )

def agregar_restaurant(request):
    if request.method == "POST":
        formulario = RestaurantFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            restaurant = Restaurant(
                nombre=data['nombre'],
                especialidad=data['especialidad'],
                direccion=data['direccion'],
                horario=data['horario'],
                )
            restaurant.save()
            url_exitosa = reverse('listar_restaurantes')
            return redirect(url_exitosa)
    else:  # GET
        formulario = RestaurantFormulario()
    return render(
        request=request,
        template_name='guia_ciudad/formulario_restaurant.html',
        context={'formulario': formulario},
    )

def buscar_restaurantes(request):
    if request.method == "POST":
        data = request.POST
        restaurantes = Restaurant.objects.filter(
            Q(nombre__contains=data['busqueda']) | Q(especialidad__contains=data['busqueda'])
        )
        contexto = {
            'restaurantes': restaurantes
        }
        return render(
            request=request,
            template_name='guia_ciudad/restaurantes.html',
            context=contexto,
        )

## VIEWS PÁGINAS DE PROPIEDADES
def listar_propiedades(request):
    contexto = {
        'propiedades': Propiedad.objects.all()
    }
    return render(
        request=request,
        template_name='guia_ciudad/propiedades.html',
        context=contexto,
    )

def agregar_propiedad(request):
    if request.method == "POST":
        formulario = PropiedadFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            propiedad = Propiedad(
                tipo=data['tipo'],
                operacion=data['operacion'],
                habitaciones=data['habitaciones'],
                precio=data['precio'],
                contacto=data['contacto'],
                )
            propiedad.save()
            url_exitosa = reverse('listar_propiedades')
            return redirect(url_exitosa)
    else:  # GET
        formulario = PropiedadFormulario()
    return render(
        request=request,
        template_name='guia_ciudad/formulario_propiedad.html',
        context={'formulario': formulario},
    )

def buscar_propiedades(request):
    if request.method == "POST":
        data = request.POST
        propiedades = Propiedad.objects.filter(
            Q(tipo__contains=data['busqueda']) | Q(operacion__contains=data['busqueda'])
        )
        contexto = {
            'propiedades': propiedades
        }
        return render(
            request=request,
            template_name='guia_ciudad/propiedades.html',
            context=contexto,
        )

## VIEWS PÁGINAS DE CLASIFICADOS
def listar_clasificados(request):
    contexto = {
        'clasificados': Clasificado.objects.all()
    }
    return render(
        request=request,
        template_name='guia_ciudad/clasificados.html',
        context=contexto,
    )

def agregar_clasificado(request):
    if request.method == "POST":
        formulario = ClasificadoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            clasificado = Clasificado(
                producto=data['producto'],
                descripcion=data['descripcion'],
                precio=data['precio'],
                contacto=data['contacto'],
                )
            clasificado.save()
            url_exitosa = reverse('listar_clasificados')
            return redirect(url_exitosa)
    else:  # GET
        formulario = ClasificadoFormulario()
    return render(
        request=request,
        template_name='guia_ciudad/formulario_clasificado.html',
        context={'formulario': formulario},
    )

def buscar_clasificados(request):
    if request.method == "POST":
        data = request.POST
        clasificados = Clasificado.objects.filter(
            Q(producto__contains=data['busqueda']) | Q(descripcion__contains=data['busqueda'])
        )
        contexto = {
            'clasificados': clasificados
        }
        return render(
            request=request,
            template_name='guia_ciudad/clasificados.html',
            context=contexto,
        )