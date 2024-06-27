from django.db import models

class Categoria(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True, default='Sin nombre')
    desc = models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripción')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class Producto(models.Model):
    codigo_producto = models.CharField(max_length=20, verbose_name='Código del producto', unique=True, default='DEFAULT_CODE')
    marca = models.CharField(max_length=50, verbose_name='Marca', default='Sin marca')
    name = models.CharField(max_length=150, verbose_name='Nombre', default='Producto sin nombre')
    cat = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoría', default=1)
    stock = models.IntegerField(default=0, verbose_name='Stock')
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name='Precio')
    imagen = models.ImageField(upload_to='productos/', default='productos/no-image.png', verbose_name='Imagen')

    def __str__(self):
        return f'{self.marca} - {self.name}'

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

class PrecioProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='precios')
    fecha = models.DateTimeField(verbose_name='Fecha')
    valor = models.IntegerField(default=0, verbose_name='Valor')

    class Meta:
        verbose_name = 'Precio del Producto'
        verbose_name_plural = 'Precios de los Productos'
        ordering = ['-fecha']
