from rest_framework import serializers
from .models import Usuario, CategoriaUsuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'nombre', 'apellido', 'correo', 'rut', 'direccion', 'telefono', 'perfil_usuario', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined']

class CategoriaUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaUsuario
        fields = ['id', 'nombrecategoria']
