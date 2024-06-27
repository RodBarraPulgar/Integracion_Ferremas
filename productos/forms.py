from django import forms
from .models import Producto

class EditarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo_producto', 'marca', 'name', 'precio', 'stock', 'cat', 'imagen']
