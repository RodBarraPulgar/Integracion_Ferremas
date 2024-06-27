from django.contrib import admin
from .models import Venta, DetalleVenta

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'buy_order', 'amount', 'transaction_date')
    search_fields = ('buy_order', 'usuario__username')

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('venta', 'producto', 'cantidad', 'precio_unitario')
    search_fields = ('venta__buy_order', 'producto__name')