# Generated by Django 5.1.1 on 2024-09-28 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_trabajador_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajador',
            name='telefono',
            field=models.BigIntegerField(verbose_name='telefono'),
        ),
    ]
