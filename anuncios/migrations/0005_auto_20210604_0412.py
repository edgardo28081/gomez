# Generated by Django 3.2 on 2021-06-04 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0004_auto_20210604_0403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promedios',
            name='porsentaje_primer_estudiante',
        ),
        migrations.RemoveField(
            model_name='promedios',
            name='porsentaje_segundo_estudiante',
        ),
        migrations.RemoveField(
            model_name='promedios',
            name='porsentaje_tercer_estudiante',
        ),
    ]