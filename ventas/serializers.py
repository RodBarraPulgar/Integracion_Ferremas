from rest_framework import serializers
from .models import Venta, DetalleVenta

class DetalleVentaSerializer(serializers.ModelSerializer):
    producto_name = serializers.CharField(source='producto.name', read_only=True)

    class Meta:
        model = DetalleVenta
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    detalles_venta = DetalleVentaSerializer(many=True, read_only=True)
    usuario = serializers.CharField(source='usuario.username', read_only=True)

    class Meta:
        model = Venta
        fields = '__all__'
