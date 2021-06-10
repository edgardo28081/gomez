from django.db import models
from tinymce import models as tinymce_models
from django.contrib.auth.models import User, Group


class Tareas_primero(models.Model):
    titulo_clase=models.CharField(max_length=100)
    telefono=models.IntegerField(max_length=11)
    whatsapp=models.IntegerField(max_length=11)
    nombre_profesor=models.CharField(max_length=50)
    correo_profesor=models.EmailField(null=True, blank=True)
    seccion=models.ForeignKey(Group, on_delete=models.PROTECT)
    contenido=tinymce_models.HTMLField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo_clase

class Tareas_segundo(models.Model):
    titulo_clase=models.CharField(max_length=100)
    telefono=models.IntegerField(max_length=11)
    whatsapp=models.IntegerField(max_length=11)
    nombre_profesor=models.CharField(max_length=50)
    correo_profesor=models.EmailField(null=True, blank=True)
    seccion=models.ForeignKey(Group, on_delete=models.PROTECT)
    contenido=tinymce_models.HTMLField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo_clase

class Tareas_tercero(models.Model):
    titulo_clase=models.CharField(max_length=100)
    telefono=models.IntegerField(max_length=11)
    whatsapp=models.IntegerField(max_length=11)
    nombre_profesor=models.CharField(max_length=50)
    correo_profesor=models.EmailField(null=True, blank=True)
    seccion=models.ForeignKey(Group, on_delete=models.PROTECT)
    contenido=tinymce_models.HTMLField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo_clase

class Tareas_cuarto(models.Model):
    titulo_clase=models.CharField(max_length=100)
    telefono=models.IntegerField(max_length=11)
    whatsapp=models.IntegerField(max_length=11)
    nombre_profesor=models.CharField(max_length=50)
    correo_profesor=models.EmailField(null=True, blank=True)
    seccion=models.ForeignKey(Group, on_delete=models.PROTECT)
    contenido=tinymce_models.HTMLField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo_clase


class Tareas_quinto(models.Model):
    titulo_clase=models.CharField(max_length=100)
    telefono=models.IntegerField(max_length=11,null=True, blank=True)
    whatsapp=models.IntegerField(max_length=11,null=True, blank=True)
    nombre_profesor=models.CharField(max_length=50)
    correo_profesor=models.EmailField(null=True, blank=True)
    seccion=models.ForeignKey(Group, on_delete=models.PROTECT)
    contenido=tinymce_models.HTMLField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo_clase
