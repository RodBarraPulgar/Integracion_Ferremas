import os
import django
import random

# Configurar la variable de entorno DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ferreplus.settings')

# Configurar Django
django.setup()

from usuarios.models import CategoriaUsuario
from productos.models import Categoria, Producto

def generar_codigo_unico(producto_nombre):
    codigo = f'{producto_nombre[:3].upper()}-{random.randint(100, 999)}'
    while Producto.objects.filter(codigo_producto=codigo).exists():
        codigo = f'{producto_nombre[:3].upper()}-{random.randint(100, 999)}'
    return codigo

def crear_categorias_y_productos():
    categorias = {
        'Herramientas': ['Martillos', 'Destornilladores', 'Llaves'],
        'Materiales de Construcción': ['Cemento', 'Arena', 'Ladrillos'],
        'Equipos de Seguridad': ['Cascos', 'Guantes', 'Lentes de Seguridad']
    }

    marcas = ['Bosch', 'Makita', 'Stanley']
    imagen_defecto = 'productos/img_defect.png'

    for categoria_nombre, productos in categorias.items():
        categoria, _ = Categoria.objects.get_or_create(name=categoria_nombre)
        for producto in productos:
            for _ in range(3):
                codigo = generar_codigo_unico(producto)
                Producto.objects.create(
                    codigo_producto=codigo,
                    marca=random.choice(marcas),
                    name=producto,
                    precio=random.uniform(10, 500),
                    stock=random.randint(1, 100),
                    imagen=imagen_defecto,
                    cat=categoria
                )

def crear_categorias_usuario():
    categorias = [
        {'nombrecategoria': 'administrador'},
        {'nombrecategoria': 'bodeguero'},
        {'nombrecategoria': 'cliente'},
        {'nombrecategoria': 'contador'},
    ]

    for categoria in categorias:
        CategoriaUsuario.objects.get_or_create(**categoria)

if __name__ == '__main__':
    crear_categorias_y_productos()
    crear_categorias_usuario()
