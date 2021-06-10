# Generated by Django 3.2 on 2021-06-08 03:13

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tareas_primro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('contenido', tinymce.models.HTMLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]