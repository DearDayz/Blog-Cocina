from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    RecetaAPIList,
    RecetaViewSet,
    IngredienteViewSet
)



urlpatterns = [
    path("recetas-list/", RecetaAPIList.as_view(), name="receta-list") #Get de todas las recetas de prueba
]

#MultiApi
router = DefaultRouter()
router.register("recetas", RecetaViewSet, basename="recetas")
router.register("ingredientes", IngredienteViewSet, basename="ingredientes")
urlpatterns += router.urls 