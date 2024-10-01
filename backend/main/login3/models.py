from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin



class MyUserManager(BaseUserManager):
    def create_user(self, username, cedula, password=None, nombre="",apellido="", direccion="", correo="", telefono=0, favoritos=dict, tipo=""):
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
            favoritos=favoritos,
            tipo=tipo,
        )

        user.set_password(password)
        user.save(using=self._db)
            
        return user

    def create_superuser(self, username, cedula, password=None, nombre="", apellido="", direccion="", correo="", telefono=0, favoritos=dict, tipo=""):
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
            favoritos=favoritos,
            tipo=tipo,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=40, default="admin")

    nombre = models.CharField(max_length=255, verbose_name="nombre", blank=True)
    apellido = models.CharField(max_length=255, verbose_name="apellido", blank=True)
    cedula = models.IntegerField(unique=True, verbose_name="cedula", blank=True)  # Asegúrate de que la cédula sea única
    direccion = models.TextField(verbose_name="direccion", blank=True)  # Para permitir texto largo
    correo = models.EmailField(max_length=255, unique=True, verbose_name="correo", blank=True)  # Asegúrate de que el correo sea único
    telefono = models.BigIntegerField(blank=True, null=True, unique=True, verbose_name="telefono")  # Cambiado a BigIntegerField para almacenar números grandes
    favoritos = models.JSONField(blank=True, null=True, verbose_name="favoritos")  # Campo para almacenar favoritos en formato JSON
    tipo = models.CharField(max_length=255, verbose_name="tipo", blank=True)

    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["nombre", "apellido", "cedula", "direccion", "correo", "telefono", "favoritos", "tipo"]

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
            ("puede_ver_vistas_admin", "Puede ver vistas administrativas"),
            # Agrega más permisos aquí según sea necesario
        )