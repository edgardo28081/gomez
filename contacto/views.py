from django import template
from django.core import mail
from django.shortcuts import render 
from .models import *




def contacto(request):


	
	
	datos=Contactos.objects.all()
	return render(request, "contacto/contacto.html", {"p":datos})
