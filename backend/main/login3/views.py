from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MyUserSerializer
from .models import MyUser
from django.contrib.auth.mixins import LoginRequiredMixin

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
            return redirect("/vista-pagina-principal/")
        else:
            return redirect("/login")
    return render(request, "login3/login.html")

# Cerrar sesión (cambiar el redirect a /home/)
def logout_user(request):
    logout(request)
    return redirect("/login/")

# Registro
class RegisterUser(APIView):
    def post(self, request):
        serializer = MyUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = authenticate(request=request, username=request.data["username"], password=request.data["password"])
        if user: login(request, user)
        return redirect("/vista-pagina-principal/")

@login_required
def user_data_view(request, username):
    # Verifica si el método es GET o POST
    if request.method == 'GET':
        # Verifica si el usuario autenticado es el mismo que el que se solicita o tiene permiso
        if request.user.username == username or request.user.has_perm("login3.ver_datos_usuario"):
            user = get_object_or_404(MyUser, username=username)
            serializer = MyUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({"error": "No puede acceder a los datos de otros usuarios"}, status=403)

    elif request.method == 'POST':
        # Verifica si el usuario autenticado es el mismo que el que se solicita o tiene permiso
        if request.user.username == username or request.user.has_perm("login3.modificar_datos_usuario"):
            user = get_object_or_404(MyUser, username=username)
            serializer = MyUserSerializer(user, data=request.POST, partial=True)  # Permite actualizaciones parciales
            if serializer.is_valid():
                serializer.save()
                return redirect("user_view")
            return Response(serializer.errors, status=400)
        else:
            return redirect("login")

    # Manejo de métodos no permitidos
    return Response({"error": "Método no permitido"}, status=405)



# Se usaba con React, se deja por si acaso
# @login_required
# def user_permissions(request):
#     permissions = request.user.get_all_permissions()
#     print(permissions)
#     return JsonResponse({'permissions': list(permissions)})