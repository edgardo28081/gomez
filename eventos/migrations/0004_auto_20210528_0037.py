# Generated by Django 3.2 on 2021-05-28 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_auto_20210527_0325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recuerdos',
            name='foto4',
        ),
        migrations.RemoveField(
            model_name='recuerdos',
            name='foto5',
        ),
        migrations.RemoveField(
            model_name='recuerdos',
            name='foto6',
        ),
    ]