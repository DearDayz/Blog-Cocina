from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("register/", views.RegisterUser.as_view(), name="register"),
    path("logout/", views.logout_user, name="logout"),
    #path("permissions/", views.user_permissions, name="permissions"),
    path("userdata/<str:username>/", views.user_data_view, name="userdata"), # Recibe peticiones GET y PATCH
]