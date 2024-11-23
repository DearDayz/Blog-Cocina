# Generated by Django 5.1.1 on 2024-11-21 20:14

import login3.validadores.validador_user
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=40, unique=True)),
                ('nombre', models.CharField(max_length=30, validators=[login3.validadores.validador_user.validar_nombre], verbose_name='nombre')),
                ('apellido', models.CharField(max_length=30, validators=[login3.validadores.validador_user.validar_nombre], verbose_name='apellido')),
                ('cedula', models.CharField(max_length=8, unique=True, validators=[login3.validadores.validador_user.validar_cedula], verbose_name='cedula')),
                ('direccion', models.TextField(validators=[login3.validadores.validador_user.validar_direccion], verbose_name='direccion')),
                ('correo', models.EmailField(max_length=255, unique=True, validators=[login3.validadores.validador_user.validar_correo], verbose_name='correo')),
                ('telefono', models.CharField(max_length=12, unique=True, validators=[login3.validadores.validador_user.validar_telefono], verbose_name='telefono')),
                ('tipo', models.CharField(max_length=20, validators=[login3.validadores.validador_user.validar_tipo], verbose_name='tipo')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'permissions': (('ver_usuario', 'Puede ver los datos de los usuarios'), ('modificar_usuario', 'Puede modificar los datos de los usuarios'), ('eliminar_usuario', 'Puede eliminar usuarios'), ('ver_facturas', 'Puede ver las facturas'), ('modificar_facturas', 'Puede modificar las facturas existentes'), ('eliminar_facturas', 'Puede eliminar facturas'), ('ver_ingredientes', 'Puede ver los ingredientes'), ('crear_ingredientes', 'Puede crear nuevos ingredientes'), ('modificar_ingredientes', 'Puede modificar los ingredientes existentes'), ('eliminar_ingredientes', 'Puede eliminar ingredientes'), ('ver_recetas', 'Puede ver las recetas'), ('crear_recetas', 'Puede crear nuevas recetas'), ('modificar_recetas', 'Puede modificar las recetas existentes'), ('eliminar_recetas', 'Puede eliminar recetas')),
            },
        ),
    ]
