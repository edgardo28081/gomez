
from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.fields.related import OneToOneField
from django.utils import timezone



class Estudiantes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='foto.png')
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    cedula = models.IntegerField(max_length=8)
    seccion=models.ForeignKey(Group, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo =models.CharField(max_length=1, choices=sexos, default='F')
    vigencia = models.BooleanField(default=True)
    nombres_representante = models.CharField(max_length=50, null=True, blank=True)
    cedula_representante = models.IntegerField(max_length=8)
    
    
    def __str__(self):
        return f'  Estudiante {self.user.username}'

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    
    
    class Meta:
        ordering = ['-timestamp']
        
    def __str__(self):
        return f'{self.user.username}: {self.content}'


class Notas_parciales_primer_Lapso(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    cedula=models.IntegerField(max_length=2)
    lapzo=models.CharField(max_length=50)
    materia=models.CharField(max_length=50, null=True, blank=True)
    nota=models.IntegerField(max_length=2, null=True, blank=True)
    materia2=models.CharField(max_length=50, null=True, blank=True)
    nota2=models.IntegerField(max_length=2, null=True, blank=True)
    materia3=models.CharField(max_length=50, null=True, blank=True)
    nota3=models.IntegerField(max_length=2, null=True, blank=True)
    materia4=models.CharField(max_length=50, null=True, blank=True)
    nota4=models.IntegerField(max_length=2, null=True, blank=True)
    materia5=models.CharField(max_length=50, null=True, blank=True)
    nota5=models.IntegerField(max_length=2, null=True, blank=True)
    materia6=models.CharField(max_length=50, null=True, blank=True)
    nota6=models.IntegerField(max_length=2, null=True, blank=True)
    materia7=models.CharField(max_length=50, null=True, blank=True)
    nota7=models.IntegerField(max_length=2, null=True, blank=True)
    materia8=models.CharField(max_length=50, null=True, blank=True)
    nota8=models.IntegerField(max_length=2, null=True, blank=True)
    materia9=models.CharField(max_length=50, null=True, blank=True)
    nota9=models.IntegerField(max_length=2, null=True, blank=True)
    materia10=models.CharField(max_length=50, null=True, blank=True)
    nota10=models.IntegerField(max_length=2, null=True, blank=True)
    materia11=models.CharField(max_length=50, null=True, blank=True)
    nota11=models.IntegerField(max_length=2, null=True, blank=True)
    materia12=models.CharField(max_length=50, null=True, blank=True)
    nota12=models.IntegerField(max_length=2, null=True, blank=True)
    materia13=models.CharField(max_length=50, null=True, blank=True)
    nota13=models.IntegerField(max_length=2, null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username

    
class Notas_parciales_segundo_Lapso(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    cedula=models.IntegerField(max_length=2)
    lapso=models.CharField(max_length=50)
    materia=models.CharField(max_length=50, null=True, blank=True)
    nota=models.IntegerField(max_length=2, null=True, blank=True)
    materia2=models.CharField(max_length=50, null=True, blank=True)
    nota2=models.IntegerField(max_length=2, null=True, blank=True)
    materia3=models.CharField(max_length=50, null=True, blank=True)
    nota3=models.IntegerField(max_length=2, null=True, blank=True)
    materia4=models.CharField(max_length=50, null=True, blank=True)
    nota4=models.IntegerField(max_length=2, null=True, blank=True)
    materia5=models.CharField(max_length=50, null=True, blank=True)
    nota5=models.IntegerField(max_length=2, null=True, blank=True)
    materia6=models.CharField(max_length=50, null=True, blank=True)
    nota6=models.IntegerField(max_length=2, null=True, blank=True)
    materia7=models.CharField(max_length=50, null=True, blank=True)
    nota7=models.IntegerField(max_length=2, null=True, blank=True)
    materia8=models.CharField(max_length=50, null=True, blank=True)
    nota8=models.IntegerField(max_length=2, null=True, blank=True)
    materia9=models.CharField(max_length=50, null=True, blank=True)
    nota9=models.IntegerField(max_length=2, null=True, blank=True)
    materia10=models.CharField(max_length=50, null=True, blank=True)
    nota10=models.IntegerField(max_length=2, null=True, blank=True)
    materia11=models.CharField(max_length=50, null=True, blank=True)
    nota11=models.IntegerField(max_length=2, null=True, blank=True)
    materia12=models.CharField(max_length=50, null=True, blank=True)
    nota12=models.IntegerField(max_length=2, null=True, blank=True)
    materia13=models.CharField(max_length=50, null=True, blank=True)
    nota13=models.IntegerField(max_length=2, null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username

class Notas_parciales_tercer_Lapso(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    cedula=models.IntegerField(max_length=2)
    lapso=models.CharField(max_length=50)
    materia=models.CharField(max_length=50, null=True, blank=True)
    nota=models.IntegerField(max_length=2, null=True, blank=True)
    materia2=models.CharField(max_length=50, null=True, blank=True)
    nota2=models.IntegerField(max_length=2, null=True, blank=True)
    materia3=models.CharField(max_length=50, null=True, blank=True)
    nota3=models.IntegerField(max_length=2, null=True, blank=True)
    materia4=models.CharField(max_length=50, null=True, blank=True)
    nota4=models.IntegerField(max_length=2, null=True, blank=True)
    materia5=models.CharField(max_length=50, null=True, blank=True)
    nota5=models.IntegerField(max_length=2, null=True, blank=True)
    materia6=models.CharField(max_length=50, null=True, blank=True)
    nota6=models.IntegerField(max_length=2, null=True, blank=True)
    materia7=models.CharField(max_length=50, null=True, blank=True)
    nota7=models.IntegerField(max_length=2, null=True, blank=True)
    materia8=models.CharField(max_length=50, null=True, blank=True)
    nota8=models.IntegerField(max_length=2, null=True, blank=True)
    materia9=models.CharField(max_length=50, null=True, blank=True)
    nota9=models.IntegerField(max_length=2, null=True, blank=True)
    materia10=models.CharField(max_length=50, null=True, blank=True)
    nota10=models.IntegerField(max_length=2, null=True, blank=True)
    materia11=models.CharField(max_length=50, null=True, blank=True)
    nota11=models.IntegerField(max_length=2, null=True, blank=True)
    materia12=models.CharField(max_length=50, null=True, blank=True)
    nota12=models.IntegerField(max_length=2, null=True, blank=True)
    materia13=models.CharField(max_length=50, null=True, blank=True)
    nota13=models.IntegerField(max_length=2, null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username


class Notas_Definitivas(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    cedula=models.IntegerField(max_length=2)
    agno=models.IntegerField(max_length=4)
    materia=models.CharField(max_length=50, null=True, blank=True)
    nota=models.IntegerField(max_length=2, null=True, blank=True)
    materia2=models.CharField(max_length=50, null=True, blank=True)
    nota2=models.IntegerField(max_length=2, null=True, blank=True)
    materia3=models.CharField(max_length=50, null=True, blank=True)
    nota3=models.IntegerField(max_length=2, null=True, blank=True)
    materia4=models.CharField(max_length=50, null=True, blank=True)
    nota4=models.IntegerField(max_length=2, null=True, blank=True)
    materia5=models.CharField(max_length=50, null=True, blank=True)
    nota5=models.IntegerField(max_length=2, null=True, blank=True)
    materia6=models.CharField(max_length=50, null=True, blank=True)
    nota6=models.IntegerField(max_length=2, null=True, blank=True)
    materia7=models.CharField(max_length=50, null=True, blank=True)
    nota7=models.IntegerField(max_length=2, null=True, blank=True)
    materia8=models.CharField(max_length=50, null=True, blank=True)
    nota8=models.IntegerField(max_length=2, null=True, blank=True)
    materia9=models.CharField(max_length=50, null=True, blank=True)
    nota9=models.IntegerField(max_length=2, null=True, blank=True)
    materia10=models.CharField(max_length=50, null=True, blank=True)
    nota10=models.IntegerField(max_length=2, null=True, blank=True)
    materia11=models.CharField(max_length=50, null=True, blank=True)
    nota11=models.IntegerField(max_length=2, null=True, blank=True)
    materia12=models.CharField(max_length=50, null=True, blank=True)
    nota12=models.IntegerField(max_length=2, null=True, blank=True)
    materia13=models.CharField(max_length=50, null=True, blank=True)
    nota13=models.IntegerField(max_length=2, null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username

class Notas_definivas2(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nota1')
    materia=models.CharField(max_length=50)
    numero=models.IntegerField(max_length=2)
    created=models.DateTimeField(auto_now_add=True)



class Notas_definivas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nota')
    materia=models.CharField(max_length=50)
    numero=models.IntegerField(max_length=2)
    created=models.DateTimeField(auto_now_add=True)
    
    
        
    def __str__(self):
        return f'{self.user.username}: {self.materia}'








