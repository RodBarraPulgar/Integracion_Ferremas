import os
import django
import random
import requests
from datetime import datetime, timedelta
from decimal import Decimal
import pytz

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ferreplus.settings')
django.setup()

from usuarios.models import Usuario
from productos.models import Producto
from ventas.models import Venta, DetalleVenta

def get_dollar_value():
    try:
        response = requests.get('https://mindicador.cl/api/dolar')
        data = response.json()
        return Decimal(str(data['serie'][0]['valor']))
    except Exception as e:
        print(f"Error al obtener el valor del dólar: {e}")
        return Decimal('1.0')  # Valor por defecto en caso de error

def generate_random_date(year, month):
    day = random.randint(1, 28 if month == 2 else 30)
    return datetime(year, month, day, tzinfo=pytz.UTC)

def populate_sales():
    # Obtener usuarios y productos de la base de datos
    usuarios = list(Usuario.objects.all())
    productos = list(Producto.objects.all())
    
    if not usuarios or not productos:
        print("Asegúrate de tener usuarios y productos en la base de datos.")
        return

    # Eliminar ventas y detalles de ventas existentes
    # DetalleVenta.objects.all().delete()
    # Venta.objects.all().delete()

    ventas_por_mes = {
        '2024-01': 20,
        '2024-02': 32,
        '2024-03': 43,
        '2024-04': 26,
        '2024-05': 21
    }

    dollar_value = get_dollar_value()

    for mes, cantidad in ventas_por_mes.items():
        year, month = map(int, mes.split('-'))
        for _ in range(cantidad):
            usuario = random.choice(usuarios)
            transaction_date = generate_random_date(year, month)
            amount = Decimal('0.0')
            detalles = []

            # Crear una venta con un valor temporal para detalles
            venta = Venta.objects.create(
                usuario=usuario,
                buy_order=f"BO-{random.randint(100000, 999999)}",
                amount=amount,
                transaction_date=transaction_date,
                detalles={}  # Inicialmente vacío
            )

            # Agregar detalles de productos
            num_products = random.randint(1, 5)
            for _ in range(num_products):
                producto = random.choice(productos)
                cantidad = random.randint(1, 10)
                precio_unitario = producto.precio * dollar_value
                detalle = DetalleVenta.objects.create(
                    venta=venta,
                    producto=producto,
                    cantidad=cantidad,
                    precio_unitario=precio_unitario,
                )
                detalles.append({
                    'producto': producto.name,
                    'cantidad': cantidad,
                    'precio_unitario': float(precio_unitario)
                })
                amount += cantidad * precio_unitario
            
            # Actualizar el monto total de la venta y los detalles
            venta.amount = amount
            venta.detalles = detalles  # Guardar los detalles en el campo JSON opcional
            venta.save()

    print("Se han creado ventas con éxito distribuidas en los meses especificados.")

if __name__ == "__main__":
    populate_sales()
