from django.contrib import admin
from .models import Producto, Factura , ProductoFacturado
# Register your models here.
#admin.site.register(Factura)
admin.site.register(Producto)
admin.site.register(Factura)
admin.site.register(ProductoFacturado)
