from django.urls import path
from views.views_carpeta.views_prueba import mostrar_html1, mostrar_receta
from .views import mostrar_principal, mostrar_entry, mostrar_buy, cart_add, logout_user
from .views import *

#Aqui configuramos las rutas de las vistas
urlpatterns = [
    path("vista-prueba/", mostrar_html1),
    path("vista-receta-prueba/<str:receta_nombre>/", mostrar_receta, name="mostrar_receta"),
    path("vista-pagina-principal/", mostrar_principal, name="vista pagina principal"),
    path("vista-entry/<int:pk>", mostrar_entry, name="vista entry"),
    path("vista-buy/", mostrar_buy, name="vista buy"),
    path('add/', cart_add, name="cart_add"),
    path('logout/', logout_user, name="logout"),

    # Login
    path('admin-view/', admin_view, name="admin"),
    path('add-recipe/', add_recipe, name="add_recipe"),
    path('user-data/', client_view, name="user_view"),
    path('login/', login_view, name="login_view"),
    path('register/', register_view, name="register_view"),
]