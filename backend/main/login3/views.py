from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MyUserSerializer
from .models import MyUser
from blog.models import Favoritos, Receta
from blog.serializers import FavoritosSerializer
from rest_framework.decorators import api_view

# Iniciar sesión (adaptarse cuando se conecte con el front)
def login_user(request):
    if request.method == "POST":
        logout(request)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request=request, username=username, password=password)

        # if user.tipo == "Administrador":
        #     permiso = Permission.objects.get(codename='puede_ver_vistas_admin')
        #     # Asignar el permiso al usuario
        #     user.user_permissions.add(permiso)

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
        if user and not request.user.is_authenticated: login(request, user)
        return redirect("/vista-pagina-principal/")

@login_required
@api_view(["GET", "POST"])
def user_data_view(request, username):
    # Verifica si el método es GET o POST
    if request.method == 'GET':
        # Verifica si el usuario autenticado es el mismo que el que se solicita o tiene permiso
        if request.user.username == username or request.user.tipo == "Administrador":
            user = get_object_or_404(MyUser, username=username)
            serializer = MyUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({"error": "No puede acceder a los datos de otros usuarios"}, status=403)

    elif request.method == 'POST':
        # Verifica si el usuario autenticado es el mismo que el que se solicita o tiene permiso
        if request.user.username == username or request.user.tipo == "Administrador":
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

@login_required
def delete_user_view(request, username):
    if request.method == 'DELETE' and request.user.tipo == "Administrador":
        user = get_object_or_404(MyUser, username=username)
        user.delete() 
        return JsonResponse({"message": "Usuario eliminado correctamente."}, status=204)
    
    return JsonResponse({"error": "Método no permitido."}, status=405)

@login_required
def favoritos_view(request, recetaId=None):
    
    # Retorna todos los favoritos del usuario de la petición
    if request.method == 'GET':
        favoritos = Favoritos.objects.filter(usuario=request.user)
        serializer = FavoritosSerializer(favoritos, many=True)
        return JsonResponse(serializer.data, safe=False)

    # Si la receta dada no está en los favoritos del usuario se agrega, si lo está, se elimina
    elif request.method == 'POST':
        if Favoritos.objects.filter(usuario=request.user, receta=recetaId).exists():
            Favoritos.objects.filter(usuario=request.user, receta=recetaId).delete()
            return JsonResponse({"message": "Receta eliminada de favoritos"}, status=204)
        elif Receta.objects.filter(id=recetaId).exists():
            nuevo_favorito = Favoritos(usuario=request.user, receta_id=recetaId)
            nuevo_favorito.save()
            return JsonResponse({"id": nuevo_favorito.id, "receta": nuevo_favorito.receta.id}, status=201)
        else:
            return JsonResponse({"error": "No se ha encontrado una receta"}, status=404)

    return JsonResponse({"error": "Método no permitido"}, status=405)

# Se usaba con React, se deja por si acaso
# @login_required
# def user_permissions(request):
#     permissions = request.user.get_all_permissions()
#     print(permissions)
#     return JsonResponse({'permissions': list(permissions)})