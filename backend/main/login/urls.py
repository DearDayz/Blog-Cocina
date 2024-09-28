from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    UsuarioViewSet,
    TrabajadorViewSet,
    UsuarioAPIRetrieveIDCard,
    TrabajadorAPIRetrieveIDCard
)

urlpatterns = [
     #endpoint que busca por cedula los usuarios
    path('usuarios/<int:cedula>/', UsuarioAPIRetrieveIDCard.as_view(), name="usuario-cedula"),
    path('trabajadores/<int:cedula>/', TrabajadorAPIRetrieveIDCard.as_view(), name="trabajor-cedula"),
]

#MultiApi
router = DefaultRouter()
router.register("usuarios", UsuarioViewSet, basename="usuarios")
router.register("trabajadores", TrabajadorViewSet, basename="trabajadores")
urlpatterns += router.urls 