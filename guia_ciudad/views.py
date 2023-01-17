from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse



def inicio(request):
    return render(
        request=request,
        template_name='guia_ciudad/inicio.html',
    )