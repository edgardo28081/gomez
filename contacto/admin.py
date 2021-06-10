from django.contrib import admin
from .models import Contactos
# Register your models here.
 
class contactos(admin.ModelAdmin):
    list_display=("telefono", "email")


admin.site.register(Contactos, contactos)
