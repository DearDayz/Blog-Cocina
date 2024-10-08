# Generated by Django 5.1.1 on 2024-10-01 15:31

import blog.validadores.validador_receta
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_receta_imagen'),
        ('ecommerce', '0003_alter_factura_cedula_alter_factura_codigo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='cantidades',
            field=models.JSONField(default=list, validators=[blog.validadores.validador_receta.validate_cantidades], verbose_name='cantidades'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='descripcion',
            field=models.TextField(validators=[django.core.validators.MaxLengthValidator(2000), blog.validadores.validador_receta.validate_no_html], verbose_name='descripcion'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/', verbose_name='Imagen'),
        ),
        migrations.RemoveField(
            model_name='receta',
            name='ingredientes',
        ),
        migrations.AlterField(
            model_name='receta',
            name='nombre',
            field=models.CharField(max_length=255, validators=[blog.validadores.validador_receta.validar_solo_letras_con_espacio, blog.validadores.validador_receta.validate_no_html], verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='preparacion',
            field=models.TextField(validators=[django.core.validators.MaxLengthValidator(5000), blog.validadores.validador_receta.validate_no_html], verbose_name='preparacion'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='puntuacion',
            field=models.FloatField(validators=[blog.validadores.validador_receta.validate_between_zero_and_five], verbose_name='puntuacion'),
        ),
        migrations.AddField(
            model_name='receta',
            name='ingredientes',
            field=models.ManyToManyField(to='ecommerce.ingrediente', verbose_name='ingredientes'),
        ),
    ]
