# Generated by Django 5.1.1 on 2024-09-28 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, verbose_name='nombre')),
                ('descripcion', models.TextField(verbose_name='descripcion')),
                ('preparacion', models.TextField(verbose_name='preparacion')),
                ('imagen', models.ImageField(upload_to='imagenes/', verbose_name='imagen')),
                ('puntuacion', models.FloatField(verbose_name='puntuacion')),
                ('ingredientes', models.JSONField(verbose_name='ingredientes')),
                ('precio', models.FloatField(verbose_name='precio')),
            ],
        ),
    ]