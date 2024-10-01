from django.contrib.auth.backends import ModelBackend
from .models import MyUser

class MyUserBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None):
        try:
            user = MyUser.objects.get(username=username)
        except MyUser.DoesNotExist:
            return None
        
        if user.check_password(password):
            user.backend = self.__module__ + '.' + self.__class__.__name__  # Asigna el backend
            return user
        return None