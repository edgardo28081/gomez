from django.shortcuts import render
from .models import Recuerdos


# Create your views here.

def recuerdos(request):

    datos=Recuerdos.objects.all()
    
    return render(request, "recuerdos/recuerdos.html", {"p":datos})


def historia(request):

    return render(request, "recuerdos/historia.html")