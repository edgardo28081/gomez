# Generated by Django 3.2 on 2021-06-08 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opciones', '0006_auto_20210608_1928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tareas_cuarto',
            old_name='secion',
            new_name='seccion',
        ),
        migrations.RenameField(
            model_name='tareas_primero',
            old_name='secion',
            new_name='seccion',
        ),
        migrations.RenameField(
            model_name='tareas_quinto',
            old_name='secion',
            new_name='seccion',
        ),
        migrations.RenameField(
            model_name='tareas_segundo',
            old_name='secion',
            new_name='seccion',
        ),
        migrations.RenameField(
            model_name='tareas_tercero',
            old_name='secion',
            new_name='seccion',
        ),
    ]