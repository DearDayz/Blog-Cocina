# Generated by Django 5.1.1 on 2024-09-28 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_receta_ingredientes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='imagen',
            field=models.ImageField(upload_to='imagenes/', verbose_name='Imagen'),
        ),
    ]