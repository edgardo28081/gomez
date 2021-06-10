from typing import Container
from django.shortcuts import render
from .models import *

# Create your views here.

def inicio(request):

    Recuerdos.objects.filter()

    
    

    return render(request, "principal/base.html")



