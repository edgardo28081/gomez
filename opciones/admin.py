from django.contrib import admin
from .models import *

class primero(admin.ModelAdmin):
    list_display=( "titulo_clase","telefono", "nombre_profesor", "seccion")


class segundo(admin.ModelAdmin):
    list_display=( "titulo_clase","telefono", "nombre_profesor", "seccion")

class tercero(admin.ModelAdmin):
    list_display=( "titulo_clase","telefono", "nombre_profesor", "seccion")

class cuarto(admin.ModelAdmin):
    list_display=( "titulo_clase","telefono", "nombre_profesor", "seccion")

class quinto(admin.ModelAdmin):
    list_display=( "titulo_clase","telefono", "nombre_profesor", "seccion")

admin.site.register(Tareas_primero, primero)

admin.site.register(Tareas_segundo, segundo)

admin.site.register(Tareas_tercero, tercero)

admin.site.register(Tareas_cuarto, cuarto)


admin.site.register(Tareas_quinto, quinto)