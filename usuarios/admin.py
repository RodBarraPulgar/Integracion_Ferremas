from django.contrib import admin
from .models import Usuario, CategoriaUsuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'rut', 'telefono')
    search_fields = ('username', 'email', 'rut')

@admin.register(CategoriaUsuario)
class CategoriaUsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombrecategoria',)
