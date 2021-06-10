from django.db import models

# Create your models here.

class Recuerdos(models.Model):
    titulo_evento=models.CharField(max_length=50)
    foto1=models.ImageField()
    contenido=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    foto2=models.ImageField()
    contenido_2=models.TextField(null=True, blank=True)
    created2=models.DateTimeField(auto_now_add=True)
    foto3=models.ImageField()
    contenido_3=models.TextField(null=True, blank=True)
    created3=models.DateTimeField(auto_now_add=True)
    foto4=models.ImageField()
    contenido_4=models.TextField(null=True, blank=True)
    created4=models.DateTimeField(auto_now_add=True)
    foto5=models.ImageField()
    contenido_5=models.TextField(null=True, blank=True)
    created5=models.DateTimeField(auto_now_add=True)
    foto6=models.ImageField()
    contenido_6=models.TextField(null=True, blank=True)
    created6=models.DateTimeField(auto_now_add=True)
    foto7=models.ImageField()
    contenido_7=models.TextField(null=True, blank=True)
    created7=models.DateTimeField(auto_now_add=True)
    foto8=models.ImageField()
    contenido_8=models.TextField(null=True, blank=True)
    created8=models.DateTimeField(auto_now_add=True)
    foto9=models.ImageField()
    contenido_9=models.TextField(null=True, blank=True)
    created9=models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name="Recuerdo"
        verbose_name_plural="Recuerdo"

    def __str__(self):
        return self.titulo_evento