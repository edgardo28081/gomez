# Generated by Django 3.2 on 2021-06-08 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opciones', '0008_auto_20210608_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='tareas_cuarto',
            name='telefono',
            field=models.IntegerField(default=1, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tareas_cuarto',
            name='whatsapp',
            field=models.IntegerField(default=1, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tareas_quinto',
            name='telefono',
            field=models.IntegerField(default=1, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tareas_quinto',
            name='whatsapp',
            field=models.IntegerField(default=1, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tareas_segundo',
            name='telefono',
            field=models.IntegerField(default=1, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tareas_segundo',
            name='whatsapp',
            field=models.IntegerField(default=1, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tareas_tercero',
            name='telefono',
            field=models.IntegerField(default=1, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tareas_tercero',
            name='whatsapp',
            field=models.IntegerField(default=1, max_length=11),
            preserve_default=False,
        ),
    ]
