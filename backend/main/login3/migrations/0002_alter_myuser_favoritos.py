# Generated by Django 5.1.1 on 2024-10-28 18:11

import login3.validadores.validador_user
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login3', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='favoritos',
            field=models.JSONField(default=dict, validators=[login3.validadores.validador_user.validar_favoritos], verbose_name='favoritos'),
        ),
    ]
