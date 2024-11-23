# Generated by Django 5.1.1 on 2024-11-23 18:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ecommerce', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='cedula', verbose_name='usuario'),
        ),
        migrations.AddField(
            model_name='productofacturado',
            name='factura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos_facturados', to='ecommerce.factura', verbose_name='factura'),
        ),
        migrations.AddField(
            model_name='productofacturado',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos_facturados', to='ecommerce.producto', verbose_name='producto_facturado'),
        ),
    ]
