# Generated by Django 3.2 on 2021-06-05 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_auto_20210605_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='notas_parciales',
            name='materia10',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='notas_parciales',
            name='materia11',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='notas_parciales',
            name='materia12',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='notas_parciales',
            name='materia13',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='notas_parciales',
            name='materia3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='notas_parciales',
            name='materia4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='notas_parciales',
            name='materia5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='notas_parciales',
            name='materia6',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='notas_parciales',
            name='materia7',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='notas_parciales',
            name='materia8',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='notas_parciales',
            name='materia9',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='notas_parciales',
            name='nota10',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='notas_parciales',
            name='nota11',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='notas_parciales',
            name='nota12',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='notas_parciales',
            name='nota13',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='notas_parciales',
            name='nota3',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='notas_parciales',
            name='nota4',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='notas_parciales',
            name='nota5',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='notas_parciales',
            name='nota6',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='notas_parciales',
            name='nota7',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='notas_parciales',
            name='nota8',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='notas_parciales',
            name='nota9',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='notas_parciales',
            name='materia',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='notas_parciales',
            name='materia2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='notas_parciales',
            name='nota',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='notas_parciales',
            name='nota2',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
    ]
