from django.db import models
from productos.models import Producto

class Venta(models.Model):
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    buy_order = models.CharField(max_length=26)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField()  # Eliminamos auto_now_add=True
    detalles = models.JSONField()  # Almacenar los detalles como JSON opcionalmente

    def __str__(self):
        return f"Venta {self.buy_order} - {self.usuario}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles_venta')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle {self.venta.buy_order} - {self.producto.name}"