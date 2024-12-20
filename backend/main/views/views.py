#funciones que renderizan los html
from decimal import Decimal
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Receta, Ingrediente, Category, Favoritos
from ecommerce.models import Producto
from .cart import Cart
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from blog.models import Receta, Ingrediente, Category, Valoracion
from .cart import Cart
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from ecommerce.models import Producto, Factura, ProductoFacturado
from login3.models import MyUser
from django.contrib import messages
from reportlab.pdfgen import canvas
from io import BytesIO
from django.utils import timezone
from reportlab.lib.pagesizes import letter
import requests
from chatbot.context import cargar_contexto_json_cliente, contexto_json_a_string


def cart_clear(request):
    if request.method == "POST":
        cart = Cart(request)
        cart.clear()

        #Pasamos la nueva longitud del carrito
        new_length = len(cart)

        return JsonResponse({"messages":"Carrito vaciado correctamente", "length": new_length}, status=200)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)

def cart_delete(request):
    cart = Cart(request)
    if request.method == "POST":
        #Obtenemos el id
        product_id = request.POST.get("product_id")

        if not(product_id and product_id.isnumeric() and int(product_id) >= 1):
            return JsonResponse({"error": "Datos invalidos"}, status=400)

        product_id = int(product_id)
        # Call delete Function in Cart
        try:
            cart.delete(product=product_id)
        except:
            return JsonResponse({"error": "Producto no encontrado"}, status=400)
        
        #Pasamos el nuevo total
        new_total = float(round(cart.card_total(), 2))
        #Pasamos la nueva longitud del carrito
        new_length = len(cart)

        response = JsonResponse({"message":"Producto eliminado correctamente", "total": new_total, "length": new_length}, status=200)
        """ messages.success(request, ("Product has Been Delete of Cart...")) """
        return response
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)


def cart_update(request):    
    cart = Cart(request)
    if request.method == "POST":
        #Obtenemos el id
        product_id = request.POST.get("product_id")
        product_qty = request.POST.get("product_qty")

        if not(product_id and product_id.isnumeric() and int(product_id) >= 1 and product_qty and es_numerico_y_mayor_que_uno(product_qty)):
            return JsonResponse({"error": "Datos invalidos"}, status=400)

        product_id = int(product_id)
        product_qty = float(product_qty)
        try:
            cart.update(product=product_id, quantity=product_qty)
        except:
            return JsonResponse({"error": "Receta no encontrada"}, status=400)
        
        #Pasamos el nuevo total
        new_total = float(round(cart.card_total(), 2))
        #Obtenemos el nuevo sub total
        new_subtotal = round(cart.get_subtotales()[str(product_id)], 2)
        
        response = JsonResponse({"message": "Cantidad actualizada correctamente", "total": new_total, "subtotal": new_subtotal}, status=200)
        """ messages.success(request, ("Your Cart Has Been Updated...")) """
        return response
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)

def create_valoracion(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            data = request.POST
            puntuacion = data.get("puntuacion")
            id_receta = data.get("id_receta")
            
            if not(puntuacion and id_receta and puntuacion.isnumeric() and id_receta.isnumeric() and int(puntuacion) <= 5 and int(puntuacion) > 0):
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
    favoritos = []
    for receta in recetas:
        if Favoritos.objects.filter(receta=receta, usuario=request.user).exists():
            favoritos.append(receta)
    if not recetas:
        return render(request, "search.html", {"input": input})
    else:
        return render(request, 'search.html', { "input": input , "recetas": recetas, "favoritos": favoritos})


def mostrar_principal(request):
    recetas = Receta.objects.all()
    categorias2 = Category.objects.all()[:3]
    favoritos = []
    for receta in recetas:
        if Favoritos.objects.filter(receta=receta, usuario=request.user).exists():
            favoritos.append(receta)
    return render(request, 'index.html', {"recetas": recetas,  "categorias2": categorias2, "favoritos": favoritos})

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
                print(product_facturados[0].subtotal)
                #Aqui quiero retornar un pdf con la factura
                # Renderizamos `buy.html` con la factura
                return render(request, 'buy.html', {
                    'factura': factura,
                    'product_facturados': product_facturados,
                    'factura_id': factura.id  # Pasamos el ID de la factura al template
                })
            else:
                messages.error(request, factura)
                messages.error(request, "Error al procesar la compra...")
                return redirect('vista pagina principal')
        else:
            return render(request, 'buy.html', {"factura_id": ""})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect("vista pagina principal")

def generar_pdf(request, factura_id):
    # Verifica que el usuario esté autenticado
    if not request.user.is_authenticated:
        return redirect("vista pagina principal")

    # Busca la factura por ID
    try:
        factura = Factura.objects.get(pk=factura_id)
        product_facturados = ProductoFacturado.objects.filter(factura=factura)
    except Factura.DoesNotExist:
        return HttpResponse("Factura no encontrada.", status=404)

    # Preparamos el PDF en memoria
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter  # tamaño de la página (8.5 x 11 pulgadas)

    # Agregar un título
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(100, height - 40, "Factura de Compra")
    
    # Información de la factura
    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, height - 60, f"Codigo de Factura: {factura.codigo}")
    pdf.drawString(100, height - 80, f"Fecha: {factura.fecha.strftime('%b. %d, %Y')}")
    pdf.drawString(100, height - 100, f"Hora: {factura.hora.strftime('%I:%M %p')}")
    pdf.drawString(100, height - 120, f"Nombre del Cliente: {factura.user.nombre} {factura.user.apellido}")
    pdf.drawString(100, height - 140, f"Cedula: {factura.user.cedula}")

    # Espacio para los productos
    pdf.drawString(100, height - 180, "Productos:")

    # Dibujar la tabla para los productos
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(100, height - 200, "Producto")
    pdf.drawString(300, height - 200, "Cantidad")
    pdf.drawString(400, height - 200, "Precio Unitario")
    pdf.drawString(500, height - 200, "Total")

    pdf.setFont("Helvetica", 10)
    y = height - 220
    for producto in product_facturados:
        pdf.drawString(100, y, producto.producto.nombre)
        pdf.drawString(300, y, f"{producto.cantidad} {producto.producto.unidad}")
        pdf.drawString(400, y, f"${producto.producto.precio:.2f} (c/{producto.producto.unidad})")
        pdf.drawString(500, y, f"${producto.subtotal:.2f}")
        y -= 20

    # Dibujar línea de separación
    pdf.line(100, y, 550, y)

    # Total de la factura
    y -= 20
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(400, y, f"Total de la Factura: ${factura.total:.2f}")

    # Finalizamos el PDF
    pdf.showPage()
    pdf.save()

    # Regresamos el archivo PDF como respuesta
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="factura_{factura.id}.pdf"'
    return response

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
    recetas = Receta.objects.filter(category__name= input)
    favoritos = []
    for receta in recetas:
        if Favoritos.objects.filter(receta=receta, usuario=request.user).exists():
            favoritos.append(receta)
    return render(request, 'catalog.html', {"recetas": recetas, "input": input, "favoritos": favoritos})

#rederizar vista chatbot

def mostrar_chatbot(request):
    response = requests.get("http://127.0.0.1:8000/blog-api/recetas/")
    cargar_contexto_json_cliente(response.json())
    contexto_json_a_string()
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

#Validacion
def es_numerico_y_mayor_que_uno(cadena):
    try:
        # Intentar convertir la cadena a un número flotante
        numero = float(cadena)
        # Verificar si es mayor o igual a 1
        return numero >= 1
    except ValueError:
        # Si no se puede convertir a float, no es numérico
        return False
    

#rederizado de vista favoritos

def view_favorites(request):
    if request.user.is_authenticated:
        favoritos = Favoritos.objects.filter(usuario=request.user)
        recetas = []
        for favorito in favoritos:
            recetas.append(favorito.receta)
        print(recetas)
        return render(request,'login/favoritos.html', {"recetas": recetas})
    else:
        redirect('login')
    

#Vista historial de facturas
def invoice_history(request):
    if request.user.is_authenticated:
        facturas = Factura.objects.filter(user = request.user)
        productos_facturados = {}
        for factura in facturas:
            productos_facturados[factura.id] = ProductoFacturado.objects.filter(factura=factura)
        return render(request,'login/historial_facturas.html', {"facturas": facturas, "productos_facturados": productos_facturados})
    else:
        redirect('login')
    
