from django.db import models
from django.db.models.fields import NullBooleanField

# Create your models here.

class Anuncios(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.TextField()
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Anuncio"
        verbose_name_plural="Anuncios"

    def __str__(self):
        return self.titulo


class Promedios(models.Model):
    foto_primer_estudiante=models.ImageField(upload_to='foto_promedios', null=True, blank=True)
    nombre_primer_estudiante=models.CharField(max_length=50)
    apellido_primer_estudiante=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    foto_segundo_estudiante=models.ImageField(upload_to='foto_promedios',null=True, blank=True)
    nombre_segundo_estudiante=models.CharField(max_length=50)
    apellido_segundo_estudiante=models.CharField(max_length=50)
    created2=models.DateTimeField(auto_now_add=True)
    foto_tercer_estudiante=models.ImageField(upload_to='foto_promedios',null=True, blank=True)
    nombre_tercer_estudiante=models.CharField(max_length=50)
    apellido_tercer_estudiante=models.CharField(max_length=50)
    created3=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Promedio"
        verbose_name_plural="Promedio"

    def __str__(self):
        return self.nombre_primer_estudiante