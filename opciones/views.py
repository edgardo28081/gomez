from django.shortcuts import render
from .models import *


def primero(request):
    datos=Tareas_primero.objects.all()

    return render(request, "tareas/primero.html", {"p":datos} )


def segundo(request):
    datos=Tareas_segundo.objects.all()

    return render(request, "tareas/segundo.html",{"p":datos})


def tercero(request):

    datos=Tareas_tercero.objects.all()

    return render(request, "tareas/tercero.html", {"p":datos})

def cuarto(request):

    datos=Tareas_cuarto.objects.all()

    return render(request, "tareas/cuarto.html", {"p":datos})

def quinto(request):
    datos=Tareas_quinto.objects.all()

    return render(request, "tareas/quinto.html", {"p":datos})
