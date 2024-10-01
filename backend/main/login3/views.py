from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MyUserSerializer
from .models import MyUser

# Iniciar sesión (adaptarse cuando se conecte con el front)
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request=request, username=username, password=password)

        if user.tipo == "Administrador":
            permiso = Permission.objects.get(codename='puede_ver_vistas_admin')
            # Asignar el permiso al usuario
            user.user_permissions.add(permiso)

        if user is not None:
            login(request, user)
            return redirect("/admin/")
        else:
            return redirect("/login3/login")
    return render(request, "login3/login.html")

# Cerrar sesión (adaptarse cuando se conecte con el front)
def logout_user(request):
    logout(request)
    return redirect("/admin/")

# Registrarse (listo para usarse con el front)
class register_user(APIView):
    def post(self, request):
        serializer = MyUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

# Retorna los permisos del usuario logeado (listo para usarse con el front) (se usará para manejar permisos en el front)
@login_required
def user_permissions(request):
    permissions = request.user.get_all_permissions()
    print(permissions)
    return JsonResponse({'permissions': list(permissions)})



#ViewSets
class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

# Endpoint que busca por cedula usando lookup_field
class UserAPIRetrieveIDCard(generics.RetrieveAPIView):
    lookup_field = 'cedula'  # Cambia el campo de búsqueda a 'cedula'
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
