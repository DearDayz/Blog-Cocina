from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    FacturaViewSet,
    IngredienteViewSet,
    IngredienteAPIRetrieveName
)


urlpatterns = [
    #endpoint que busca por nombre los ingredientes
    path('ingredientes/<str:nombre>/', IngredienteAPIRetrieveName.as_view(), name="ingrediente-nombre"),
]

#MultiApi
router = DefaultRouter()
router.register("facturas", FacturaViewSet, basename="facturas")
router.register("ingredientes", IngredienteViewSet, basename="ingredientes")
urlpatterns += router.urls 