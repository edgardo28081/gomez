from django.db import models

# Create your models here.

class Recuerdos(models.Model):
    titulo_evento=models.CharField(max_length=100, null=True, blank=True)
    foto1=models.ImageField(upload_to='recuerdos', null=True, blank=True)
    foto2=models.ImageField(upload_to='recuerdos', null=True, blank=True)
    foto3=models.ImageField(upload_to='recuerdos', null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Recuerdo"
        verbose_name_plural="recurdo"