from rest_framework import generics
from .models import Producto,Factura, ProductoFacturado
from .serializers import ProductoSerializer, FacturaSerializer, ProductoFacturadoSerializer
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample
from .tables import get_table_ingrediente, get_example_ingrediente, post_table_ingrediente, post_example_ingrediente, get_table_factura, get_example_factura, post_table_factura, post_example_factura
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from login3.models import MyUser

# Create your views here.

#ViewSets

#Ingredientes
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    @extend_schema(
        responses={
            200: OpenApiResponse(
                description=get_table_ingrediente,
                response=ProductoSerializer(many=True),  # Documentar usando el serializer asda
                examples=[
                    OpenApiExample(
                        'Ejemplo de Obtencion de un get',
                        value=get_example_ingrediente)]
            ),
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    
    @extend_schema(
        request=ProductoSerializer,  # Documentar el request usando el serializer
        responses={
            201: OpenApiResponse(
                description=post_table_ingrediente,
                response=ProductoSerializer(),
                examples=[
                    OpenApiExample(
                        'Ejemplo de cuerpo de solicitud',
                        value=[post_example_ingrediente]
                    )
                ]
            ),
            400: OpenApiResponse(
                description='Error de validación',
            ),
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

# Endpoint que busca por nombre usando lookup_field
class ProductoAPIRetrieveName(generics.RetrieveAPIView):
    lookup_field = 'nombre'  # Cambia el campo de búsqueda a 'nombre'
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer



#Facturas
class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    def get_serializer_class(self):
        if self.request and self.request.method in ['POST']:
            return FacturaSerializer  # Usa el serializer de creación para POST
        return FacturaSerializer  # Usa el serializer de lectura para GET
    
    @extend_schema(
        responses={
            200: OpenApiResponse(
                description=get_table_factura,
                response=FacturaSerializer(many=True),  # Documentar usando el serializer asda
                examples=[
                    OpenApiExample(
                        'Ejemplo de Obtencion de un get',
                        value=get_example_factura)]
            ),
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(
        request=FacturaSerializer,  # Documentar el request usando el serializer
        responses={
            201: OpenApiResponse(
                description=post_table_factura,
                response=FacturaSerializer(),
                examples=[
                    OpenApiExample(
                        'Ejemplo de cuerpo de solicitud',
                        value=[post_example_factura]
                    )
                ]
            ),
            400: OpenApiResponse(
                description='Error de validación',
            ),
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class FacturaAPIRetrieveByCedula(generics.ListAPIView):
    serializer_class = FacturaSerializer

    def get_queryset(self):
        cedula = self.kwargs.get('cedula')
        return Factura.objects.filter(cedula=cedula)

class ProductoFacturadoViewSet(viewsets.ModelViewSet):
    queryset = ProductoFacturado.objects.all()
    serializer_class = ProductoFacturadoSerializer

@csrf_exempt
def procesar_compra(request):
    if request.method == "POST":
        try:
            # Decodificar el cuerpo de la solicitud JSON
            data = json.loads(request.body)
            productos = data.get("productos", [])
            productos_dict = {}

            for producto in productos:
                id_producto = producto["id"]
                cantidad = producto["cantidad"]

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
                total += producto.precio * producto_list["cantidad"]
                if producto.cantidad_disponible < producto_list["cantidad"]:
                    band = False
                    producto_no_stock = producto.nombre
                    disponible =  producto.cantidad_disponible
                    unidad = producto.unidad
                    break

            if band:
                user = MyUser.objects.get(cedula=data["cedula"])
                factura  = Factura.objects.create(user=user, total=total)
                for producto_list in productos_list:
                    producto = Producto.objects.get(id=producto_list["id"])
                    ProductoFacturado.objects.create(factura=factura, producto=producto, cantidad=producto_list["cantidad"])
                    producto.cantidad_disponible -= producto_list["cantidad"]
                    producto.unidades_vendidas += producto_list["cantidad"]
                    producto.save()
                return JsonResponse({"message": "Compra realizada con éxito", "factura": factura.codigo}, status=201)
            else:
                return JsonResponse({"message": f"No hay stock del producto {producto_no_stock}, queda disponible {disponible}{unidad}"}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Cuerpo de solicitud no válido, debe ser JSON"}, status=400)
        except Producto.DoesNotExist:
            return JsonResponse({"error": "Producto no encontrado"}, status=404)
        except KeyError:
            return JsonResponse({"error": "Datos faltantes en la solicitud"}, status=400)

    return JsonResponse({"error": "Método no permitido"}, status=405)


    

    




