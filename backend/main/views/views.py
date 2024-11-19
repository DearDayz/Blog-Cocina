#funciones que renderizan los html
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Receta, Ingrediente, Category
from ecommerce.models import Producto
from .cart import Cart
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def mostrar_principal(request):
    recetas = Receta.objects.all()
    categorias = Category.objects.all()
    name_categorias = [ c.name.replace(" ", "-") for c in categorias ]
    return render(request, 'index.html', {"recetas": recetas, "categorias": categorias, "name_categorias": name_categorias})

def mostrar_entry(request, pk):
    receta = Receta.objects.get(id=pk)
    last_recetas = Receta.objects.all().order_by('-date_modified')[:3]
    ingredientes = Ingrediente.objects.filter(receta=pk)
    return render(request, 'entry.html', {"receta": receta, "ingredientes": ingredientes, "last_recetas": last_recetas})

def mostrar_buy(request):
    if request.user.is_authenticated:
        return render(request, 'buy.html')
    else:
        return redirect("vista pagina principal")

def cart_add(request):
    #Obtenemos el cart de la request
    cart = Cart(request)
    #verificamos si es post
    if request.POST.get("action") == "post":
        #Obtenemos el id
        receta_id = int(request.POST.get("receta_id"))
        receta_qty =  int(request.POST.get("receta_qty"))
        #Obtenemos el producto
        receta = get_object_or_404(Receta, id=receta_id)
        #Añadimos el producto al cart
        cart.add(receta=receta, quantity = receta_qty)
        #Retornamos un response
        
        #Get Cart Quantity
        cart_quantity =  len(cart)
        
        # response = JsonResponse({'Product Name: ': product.name})
        #messages.success(request, ("Product Added To Cart..."))
        response = JsonResponse({'qty': cart_quantity})
        return response
    else:
        return redirect('home')

def logout_user(request):
    logout(request)
    #messages.success(request, ("You have been logged out...Thanks"))
    return redirect('vista pagina principal')


# Rutas del login

def admin_view(request):
    return render(request, "login/Administrador_jefe.html")

@login_required
def add_recipe(request):
    categorias = Category.objects.all()
    productos = Producto.objects.all()
    categorias_lista = [
        {
            "id": c.id,
            "name": c.name,
        }
        for c in categorias
    ]
    productos_lista = [
        {
            "id": p.id,
            "nombre": p.nombre,
        }
        for p in productos
    ]
    return render(request, "login/Agregar_receta.html", {"categorias": categorias_lista, "productos": productos_lista})

@login_required
def client_view(request):
    if request.user.is_authenticated:
        return render(request, "login/Cliente.html", {"user": request.user})
    else:
        return redirect("login_view")
    
def login_view(request):
    return render(request, "login/login.html")

def register_view(request):
    return render(request, "login/registrar_cuenta.html")

@login_required
def modify_user_data_view(request):
    return render(request, "login/registrar_cuenta.html")