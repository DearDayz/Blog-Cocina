#funciones que renderizan los html
from decimal import Decimal
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Receta, Ingrediente, Category
from ecommerce.models import Producto
from .cart import Cart
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from blog.models import Receta, Ingrediente, Category, Valoracion
from .cart import Cart
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from ecommerce.models import Producto, Factura, ProductoFacturado
from login3.models import MyUser
from django.contrib import messages


def create_valoracion(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            data = request.POST
            puntuacion = data.get("puntuacion")
            id_receta = data.get("id_receta")
            
            if not(puntuacion or id_receta or puntuacion.isnumeric() or id_receta.isnumeric() or int(puntuacion) > 5 or int(puntuacion) < 0):
                return JsonResponse({"error": "Datos invalidos"}, status=400)
            else:
                receta = get_object_or_404(Receta, id=id_receta)
                try:
                    valoracion = Valoracion.objects.get(user=request.user, receta=receta)
                    valoracion.puntuacion = int(puntuacion)
                    valoracion.save()
                except:
                    Valoracion.objects.create(user=request.user, receta=receta, puntuacion=int(puntuacion))
                return JsonResponse({"success": "Valoracion hecha correctamente"}, status=200)

        else:
            return JsonResponse({"error": "Método no permitido"}, status=405)
    else:
        messages.error(request, "Debes estar logeado para valorar...")
        return redirect('login')

def search(request, input):
    input = input.replace("-", " ")
    recetas = Receta.objects.filter(Q(nombre__icontains = input) | Q(descripcion__icontains=input) | Q(preparacion__icontains=input))
    if not recetas:
        return render(request, "search.html", {"input": input})
    else:
        return render(request, 'search.html', { "input": input , "recetas": recetas})


def mostrar_principal(request):
    categorias1 = Category.objects.all()
    categ_dict = {}
    for categoria in categorias1:
        categ_dict[categoria.name.replace(" ", "-")] = categoria.name
    recetas = Receta.objects.all()
    categorias2 = Category.objects.all()[:3]
    return render(request, 'index.html', {"recetas": recetas,  "categorias2": categorias2  ,"categ_dict": categ_dict})

def mostrar_entry(request, pk):
    receta = Receta.objects.get(id=pk)
    last_recetas = Receta.objects.all().order_by('-date_modified')[:3]
    ingredientes = Ingrediente.objects.filter(receta=pk)
    if request.user.is_authenticated:
        #Existe valoracion por parte del usuario
        valoracion = Valoracion.objects.filter(user=request.user, receta=receta)
        try:
            valoracion = Valoracion.objects.get(user=request.user, receta=receta)
            valoracion = valoracion.puntuacion
        except Valoracion.DoesNotExist:
            valoracion = 0
    else:
        valoracion = 0
    
    #Estrellas no marcadas
    star = range(valoracion + 1, 6)

    #Estrellas marcadas
    stars_valoradas = range(1,valoracion+1)
    return render(request, 'entry.html', {"receta": receta, "ingredientes": ingredientes, "last_recetas": last_recetas, "stars_valoradas": stars_valoradas, "star": star})

def mostrar_buy(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            productos = request.session.get('session_key')
            diccionario = { "productos": productos, "cedula": request.user.cedula }
            factura = procesar_compra(diccionario, request)
            if not(type(factura) == type(str())):
                request.session['session_key'] = {}
                request.session.modified = True
                product_facturados = ProductoFacturado.objects.filter(factura=factura)
                return render(request, 'buy.html', {'factura': factura, 'product_facturados': product_facturados})
            else:
                messages.error(request, factura)
                messages.error(request, "Error al procesar la compra...")
                return redirect('vista pagina principal')
        else:
            return render(request, 'buy.html')
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
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

@login_required
def manage_recipes(request):
    if request.user.tipo == "Administrador":
        return render(request, "login/Admin_Recetas.html")
    else:
        return redirect("login_view")
    
@login_required
def admin_view_recipes(request):
    if request.user.tipo == "Administrador":
        recetas = Receta.objects.all()
        return render(request, "login/Recetas_Detalles.html", {"recetas": recetas})
    else:
        return redirect("login_view")

#rederizar vista catalog
def mostrar_catalog(request, input):
    input = input.replace("-" , " ")
    categ_dict = {}
    categorias = Category.objects.all()
    for categoria in categorias:
        categ_dict[categoria.name.replace(" ", "-")] = categoria.name
    recetas = Receta.objects.filter(category__name= input)

    return render(request, 'catalog.html', {"recetas": recetas, "categ_dict": categ_dict})

#rederizar vista chatbot

def mostrar_chatbot(request):
    # response = requests.get("http://127.0.0.1:8000/blog-api/recetas/")
    # print(response.json())
    # tabla = {"recetas": response.json()}
    # cargar_contexto_json_cliente(tabla)
    # contexto_json_a_string()
    return render(request, 'chatbot.html')


def procesar_compra(data, request):
    productos = data.get("productos")
    productos_dict = {}

    for key,value in productos.items():
        id_producto = key
        cantidad = value
        if id_producto not in productos_dict:
            productos_dict[id_producto] = 0
        productos_dict[id_producto] += cantidad

    productos_list = [{"id": id_producto, "cantidad": cantidad} for id_producto, cantidad in productos_dict.items()]
    band = True
    producto_no_stock = ""
    total = 0
    disponible = float()
    unidad = str()
    for producto_list in productos_list:
        producto = Producto.objects.get(id=producto_list["id"])
        total += float(producto.precio) * producto_list["cantidad"]
        if producto.cantidad_disponible < producto_list["cantidad"]:
            band = False
            producto_no_stock = producto.nombre
            disponible =  producto.cantidad_disponible
            unidad = producto.unidad
            break

    if band:
        user = MyUser.objects.get(cedula=data["cedula"])
        factura  = Factura.objects.create(user=user, total=round(total, 2))
        for producto_list in productos_list:
            producto = Producto.objects.get(id=producto_list["id"])
            ProductoFacturado.objects.create(factura=factura, producto=producto, cantidad=producto_list["cantidad"], subtotal=Decimal( float(producto.precio) * producto_list["cantidad"]))
            producto.cantidad_disponible -= producto_list["cantidad"]
            producto.unidades_vendidas += Decimal(producto_list["cantidad"])
            producto.save()
        factura.save()
        return factura
    else:
        return f"El producto {producto_no_stock} no tiene stock suficiente. Disponible: {disponible} {unidad}"
