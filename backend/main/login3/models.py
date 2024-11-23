from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

from .validadores import validador_user as val

class MyUserManager(BaseUserManager):
    def create_user(self, username, cedula, password=None, nombre="",apellido="", direccion="", correo="", telefono="", tipo=""):
        """
        Creates and saves a User
        """
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            username=username,
            cedula=cedula,
            nombre=nombre,
            apellido=apellido,
            direccion=direccion,
            correo=correo,
            telefono=telefono,
            tipo=tipo,
        )

        user.set_password(password)
        user.save(using=self._db)
            
        return user

    def create_superuser(self, username, cedula, password=None, nombre="", apellido="", direccion="", correo="", telefono="", tipo=""):
        """
        Creates and saves a superuser
        """
        user = self.create_user(
            username=username,
            password=password,
            nombre=nombre,
            cedula=cedula,
            apellido=apellido,
            direccion=direccion,
            correo=correo,
            telefono=telefono,
            tipo=tipo,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=40)

    nombre = models.CharField(max_length=30, verbose_name="nombre", validators=[val.validar_nombre])
    apellido = models.CharField(max_length=30, verbose_name="apellido", validators=[val.validar_nombre])
    cedula = models.CharField(max_length=8, unique=True, verbose_name="cedula", validators=[val.validar_cedula])  
    direccion = models.TextField(verbose_name="direccion", validators=[val.validar_direccion])  
    correo = models.EmailField(max_length=255, unique=True, verbose_name="correo", validators=[val.validar_correo]) 
    telefono = models.CharField(max_length=12, unique=True, verbose_name="telefono", validators=[val.validar_telefono])
    tipo = models.CharField(max_length=20, verbose_name="tipo", validators=[val.validar_tipo])

    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["nombre", "apellido", "cedula", "direccion", "correo", "telefono", "tipo"]

    def __str__(self):
        return f"{self.nombre} {self.apellido} - cedula: {self.cedula} - tipo: {self.tipo}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        permisos = self.get_all_permissions()
        
        return perm in permisos
    
    def add_permission(self, perm):
        self.user_permissions.add(perm)

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    class Meta:
        permissions = (
            ("ver_usuario", "Puede ver los datos de los usuarios"),
            ("modificar_usuario", "Puede modificar los datos de los usuarios"),
            ("eliminar_usuario", "Puede eliminar usuarios"),
            ("ver_facturas", "Puede ver las facturas"),
            ("modificar_facturas", "Puede modificar las facturas existentes"),
            ("eliminar_facturas", "Puede eliminar facturas"),
            ("ver_ingredientes", "Puede ver los ingredientes"),
            ("crear_ingredientes", "Puede crear nuevos ingredientes"),
            ("modificar_ingredientes", "Puede modificar los ingredientes existentes"),
            ("eliminar_ingredientes", "Puede eliminar ingredientes"),
            ("ver_recetas", "Puede ver las recetas"),
            ("crear_recetas", "Puede crear nuevas recetas"),
            ("modificar_recetas", "Puede modificar las recetas existentes"),
            ("eliminar_recetas", "Puede eliminar recetas"),
        )