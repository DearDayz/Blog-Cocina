from django.urls import path
from views.views_carpeta.views_prueba import mostrar_html1, mostrar_receta
from .views import *

#Aqui configuramos las rutas de las vistas
urlpatterns = [
    path("vista-prueba/", mostrar_html1),
    path("vista-receta-prueba/<str:receta_nombre>/", mostrar_receta, name="mostrar_receta"),
    path("vista-pagina-principal/", mostrar_principal, name="vista pagina principal"),
    path("vista-entry/<int:pk>", mostrar_entry, name="vista entry"),
    path("vista-buy/", mostrar_buy, name="vista buy"),
    path('add/', cart_add, name="cart_add"),
    path('search/<str:input>/', search, name="search"),
    path('catalog/<str:input>/', mostrar_catalog, name="catalog"),
    path('chatbot_produccion/', mostrar_chatbot, name="chatbot_produccion"),
    path('create_valoracion/', create_valoracion, name="create_valoracion"),
    path('cart_update/', cart_update, name="cart_update"),
    path('cart_delete/', cart_delete, name="cart_delete"),
    path('cart_clear/', cart_clear, name="cart_clear"),
    path('generar-pdf/<int:factura_id>/', generar_pdf, name='generar_pdf'),

    # Login
    path('admin-view/', admin_view, name="admin"),
    path('add-recipe/', add_recipe, name="add_recipe"),
    path('user-data/', client_view, name="user_view"),
    path('login/', login_view, name="login_view"),
    path('register/', register_view, name="register_view"),
    path('logout/', logout_user, name="logout"),
    path('manage-recipes/', manage_recipes, name="manage-recipes"),
    path('admin-view-recipes/', admin_view_recipes, name="admin-view-recipes"),
    
    
]