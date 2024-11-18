#funciones que renderizan los html
from decimal import Decimal
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Receta, Ingrediente, Category
from .cart import Cart
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from ecommerce.models import Producto, Factura, ProductoFacturado
from login3.models import MyUser
from django.contrib import messages

def search(request, input):
    input = input.replace("-", " ")
    recetas = Receta.objects.filter(Q(nombre__icontains = input) | Q(descripcion__icontains=input) | Q(preparacion__icontains=input))
    if not recetas:
        return render(request, "search.html", {"input": input})
    else:
        return render(request, 'search.html', { "input": input , "recetas": recetas})


def mostrar_principal(request):
    categorias = Category.objects.all()
    categ_dict = {}
    for categoria in categorias:
        categ_dict[categoria.name.replace(" ", "-")] = categoria.name
    recetas = Receta.objects.all()
    categorias = Category.objects.all()
    return render(request, 'index.html', {"recetas": recetas, "categorias": categorias, "categ_dict": categ_dict})

def mostrar_entry(request, pk):
    receta = Receta.objects.get(id=pk)
    last_recetas = Receta.objects.all().order_by('-date_modified')[:3]
    ingredientes = Ingrediente.objects.filter(receta=pk)
    return render(request, 'entry.html', {"receta": receta, "ingredientes": ingredientes, "last_recetas": last_recetas})

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