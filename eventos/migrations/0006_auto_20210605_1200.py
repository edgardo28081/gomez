# Generated by Django 3.2 on 2021-06-05 16:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0005_auto_20210528_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='recuerdos',
            name='contenido_4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='contenido_5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='contenido_6',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='contenido_7',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='contenido_8',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='contenido_9',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='created2',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='created3',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='created4',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='created5',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='created6',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='created7',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='created8',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='created9',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='foto4',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='foto5',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='foto6',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='foto7',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='foto8',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='foto9',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='titulo_evento2',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='titulo_evento3',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='titulo_evento4',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='titulo_evento5',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='titulo_evento6',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='titulo_evento7',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='titulo_evento8',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recuerdos',
            name='titulo_evento9',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
