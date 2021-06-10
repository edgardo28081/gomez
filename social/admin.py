from social.views import notas
from django.contrib import admin
from .models import *
# Register your models here.

class datosestudiantes(admin.ModelAdmin):
    list_display=("user", "nombre", "apellido", "seccion", "image")
    
    search_fields=('apellido', 'cedula')


class datosparciales(admin.ModelAdmin):
    list_display=("user", "lapzo", "materia", "nota")
    search_fields=("cedula", "materia")
    
   
class datosparciales2(admin.ModelAdmin):
    list_display=("user", "lapso", "materia", "nota")
    search_fields=("cedula", "materia")
    
    
class datosparcialis(admin.ModelAdmin):
    
    list_display=("user", "lapso", "materia", "nota")
    search_fields=("cedula", "materia")
    

class datosparcial(admin.ModelAdmin):
    
    list_display=("user", "agno", "materia", "nota")
    search_fields=("cedula", "materia")
    

admin.site.register(Estudiantes, datosestudiantes)

admin.site.register(Notas_parciales_primer_Lapso, datosparciales)

admin.site.register(Notas_parciales_segundo_Lapso, datosparciales2)

admin.site.register(Notas_parciales_tercer_Lapso, datosparcialis)

admin.site.register(Notas_Definitivas, datosparcial)


