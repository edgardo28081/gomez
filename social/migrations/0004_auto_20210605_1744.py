# Generated by Django 3.2 on 2021-06-05 21:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0003_auto_20210605_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notas_parciales',
            name='user',
        ),
        migrations.AddField(
            model_name='notas_parciales',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
