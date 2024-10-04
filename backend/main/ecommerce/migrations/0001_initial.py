# Generated by Django 5.1.1 on 2024-09-28 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=255)),
                ('cedula', models.IntegerField()),
                ('ingredientes', models.JSONField()),
                ('total', models.FloatField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('hora', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre')),
                ('unidad', models.CharField(max_length=50, verbose_name='unidad')),
                ('cantidad_disponible', models.FloatField(verbose_name='cantidad_disponible')),
                ('precio', models.FloatField(verbose_name='precio')),
                ('unidades_vendidas', models.FloatField(verbose_name='unidades_vendidas')),
            ],
        ),
    ]