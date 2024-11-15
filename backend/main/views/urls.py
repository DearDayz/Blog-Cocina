from django.urls import path
from views.views_carpeta.views_prueba import mostrar_html1, mostrar_receta
from .views import mostrar_principal, mostrar_entry, mostrar_buy

#Aqui configuramos las rutas de las vistas
urlpatterns = [
    path("vista-prueba/", mostrar_html1),
    path("vista-receta-prueba/<str:receta_nombre>/", mostrar_receta, name="mostrar_receta"),
    path("vista-pagina-principal/", mostrar_principal, name="vista pagina principal"),
    path("vista-entry/", mostrar_entry, name="vista entry"),
    path("vista-buy/", mostrar_buy, name="vista buy"),


    
]