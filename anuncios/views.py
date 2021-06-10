from django.shortcuts import render
from .models import *

# Create your views here.

def anuncios(request):

    datos=Anuncios.objects.all()

    context={
        "p": datos
    }

    return render(request, "anuncios/anuncios.html", context)

def promedios(request):

    datos2=Promedios.objects.all()

    context={
        "p": datos2
    }

    return render(request, "anuncios/promedios.html", context)

   
  