from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MyUserSerializer
from .models import MyUser

# Iniciar sesión (adaptarse cuando se conecte con el front)
def login_user(request):
    if request.method == "POST":
        logout(request)
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

# Cerrar sesión (cambiar el redirect a /home/)
def logout_user(request):
    logout(request)
    return redirect("/admin/")

# Registro
class RegisterUser(APIView):
    def post(self, request):
        serializer = MyUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

@login_required
class UserDataView(APIView):
    # Obtener datos de un usuario solo si es el mismo de la solicitud o se tiene el permiso
    def get(self, request, username, format=None):
        if request.user.username == username or request.user.has_perm("login3.ver_datos_usuario"):
            try:
                user = MyUser.objects.get(username=username)
                serializer = MyUserSerializer(user)
                return Response(serializer.data)
            except MyUser.DoesNotExist:
                return Response({"error": "User not found"}, status=404)
        else:
            return Response({"error", "No puede acceder a los datos de otros usuarios"}, status=403)
        
    def patch(self, request, username, format=None):
    # Modificar datos de un usuario solo si es el mismo de la solicitud o se tiene el permiso
        if request.user.username == username or request.user.has_perm("login3.modificar_datos_usuario"):
            try:
                user = MyUser.objects.get(username=username)
                serializer = MyUserSerializer(user, data=request.data, partial=True)  # partial=True permite actualizaciones parciales
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=400)
            except MyUser.DoesNotExist:
                return Response({"error": "User not found"}, status=404)
        else:
            return Response({"error", "No puede acceder a los datos de otros usuarios"}, status=403)



# Se usaba con React, se deja por si acaso
# @login_required
# def user_permissions(request):
#     permissions = request.user.get_all_permissions()
#     print(permissions)
#     return JsonResponse({'permissions': list(permissions)})