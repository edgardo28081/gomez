from django.contrib import admin
from .models import *

# Register your models here.
class promedios(admin.ModelAdmin):
    readonly_fields=("created")

admin.site.register(Anuncios)
admin.site.register(Promedios)