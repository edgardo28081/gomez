# Generated by Django 3.2 on 2021-06-07 00:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0013_notas_parciales_segundo_lapso_notas_parciales_tercer_lapso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notas_Definitivas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.IntegerField(max_length=2)),
                ('agno', models.IntegerField(max_length=4)),
                ('materia', models.CharField(blank=True, max_length=50, null=True)),
                ('nota', models.IntegerField(blank=True, max_length=2, null=True)),
                ('materia2', models.CharField(blank=True, max_length=50, null=True)),
                ('nota2', models.IntegerField(blank=True, max_length=2, null=True)),
                ('materia3', models.CharField(blank=True, max_length=50, null=True)),
                ('nota3', models.IntegerField(blank=True, max_length=2, null=True)),
                ('materia4', models.CharField(blank=True, max_length=50, null=True)),
                ('nota4', models.IntegerField(blank=True, max_length=2, null=True)),
                ('materia5', models.CharField(blank=True, max_length=50, null=True)),
                ('nota5', models.IntegerField(blank=True, max_length=2, null=True)),
                ('materia6', models.CharField(blank=True, max_length=50, null=True)),
                ('nota6', models.IntegerField(blank=True, max_length=2, null=True)),
                ('materia7', models.CharField(blank=True, max_length=50, null=True)),
                ('nota7', models.IntegerField(blank=True, max_length=2, null=True)),
                ('materia8', models.CharField(blank=True, max_length=50, null=True)),
                ('nota8', models.IntegerField(blank=True, max_length=2, null=True)),
                ('materia9', models.CharField(blank=True, max_length=50, null=True)),
                ('nota9', models.IntegerField(blank=True, max_length=2, null=True)),
                ('materia10', models.CharField(blank=True, max_length=50, null=True)),
                ('nota10', models.IntegerField(blank=True, max_length=2, null=True)),
                ('materia11', models.CharField(blank=True, max_length=50, null=True)),
                ('nota11', models.IntegerField(blank=True, max_length=2, null=True)),
                ('materia12', models.CharField(blank=True, max_length=50, null=True)),
                ('nota12', models.IntegerField(blank=True, max_length=2, null=True)),
                ('materia13', models.CharField(blank=True, max_length=50, null=True)),
                ('nota13', models.IntegerField(blank=True, max_length=2, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
