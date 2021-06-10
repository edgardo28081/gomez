from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User



def profile(request, username=None):
	current_user = request.user
	if username and username != current_user.username:
		user = User.objects.get(username=username)
		posts = user.posts.all()
	else:
		posts = current_user.posts.all()
		user = current_user
	return render(request, 'estudiantes/datos.html', {'user':user, 'posts':posts})


def estudiantes(request):

	posts=Post.objects.all()

	

	return render(request, "estudiantes/estudiantes.html",{ 'posts':posts})


def notas(request, username=None):
	current_user2 = request.user
	if username and username != current_user2.username:
		user = User.objects.get(username=username)
		nota = user.nota.all()
	else:
		nota = current_user2.nota.all()
		user = current_user2
	return render(request, 'estudiantes/notas1.html', {'user':user, 'nota':nota})


def notas_definitivas(request, username=None):

	current_user2 = request.user
	if username and username != current_user2.username:
		user = User.objects.get(username=username)
		nota1 = user.nota1.all()
	else:
		nota1 = current_user2.nota.all()
		user = current_user2
	
	return  render(request, "estudiantes/nostas.html", {'user':user, 'nota':nota1})