from django.contrib import admin
from .models import Receta, Ingrediente, Category, Valoracion, Favoritos
# Register your models here.
admin.site.register(Receta)
admin.site.register(Ingrediente)
admin.site.register(Category)
admin.site.register(Valoracion)
admin.site.register(Favoritos)