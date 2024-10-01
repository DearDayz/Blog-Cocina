from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("register/", views.register_user.as_view(), name="register"),
    path("logout/", views.logout_user, name="logout"),
    path("permissions/", views.user_permissions, name="permissions"),

     #endpoint que busca por cedula los usuarios
    path('usuarios/<int:cedula>/', views.UserAPIRetrieveIDCard.as_view(), name="usuario-cedula"),
]

#MultiApi
router = DefaultRouter()
router.register("usuarios", views.UserViewSet, basename="usuarios")
urlpatterns += router.urls 