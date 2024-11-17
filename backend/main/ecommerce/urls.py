from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (

    ProductoViewSet,
    ProductoAPIRetrieveName,
    FacturaAPIRetrieveByCedula,
    FacturaViewSet,
    ProductoFacturadoViewSet
)

    


urlpatterns = [
    #endpoint que busca por nombre los producto
    path('producto-nombre/<str:nombre>/', ProductoAPIRetrieveName.as_view(), name="producto-nombre"),
    path('factura-cedula/<str:cedula>/', FacturaAPIRetrieveByCedula.as_view(), name="factura-cedula"),

]

#MultiApi
router = DefaultRouter()

router.register("facturas", FacturaViewSet, basename="facturas")
router.register("productos", ProductoViewSet, basename="productos")
router.register("productos-facturados", ProductoFacturadoViewSet, basename="productos-facturados")
urlpatterns += router.urls 