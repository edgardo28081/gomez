from django.db import models

# Create your models here.

class Contactos(models. Model):
    telefono=models.IntegerField(max_length=11)
    email=models.EmailField()

    class Meta:
        verbose_name="Contato"
        verbose_name_plural="Contacto"

    def __str__(self):
        return self.email
