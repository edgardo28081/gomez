# Generated by Django 3.2 on 2021-05-28 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0004_auto_20210528_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='recuerdos',
            name='contenido_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='contenido_3',
            field=models.TextField(blank=True, null=True),
        ),
    ]
