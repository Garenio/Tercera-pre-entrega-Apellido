from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from guia_ciudad.models import Comercio, Restaurant, Propiedad, Clasificado



def inicio(request):
    return render(
        request=request,
        template_name='guia_ciudad/inicio.html',
    )

def listar_comercios(request):
    contexto = {
        'comercios': Comercio.objects.all()
    }
    return render(
        request=request,
        template_name='guia_ciudad/comercios.html',
        context=contexto,
    )