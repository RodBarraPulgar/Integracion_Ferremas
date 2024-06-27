from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import JsonResponse
from django.core.exceptions import PermissionDenied
from .forms import EditarProductoForm
from .models import Producto, Categoria, PrecioProducto
from .serializers import ProductoSerializer, CategoriaSerializer, PrecioProductoSerializer
from rest_framework import generics

def check_admin_or_bodeguero(user):
    if user.perfil_usuario.nombrecategoria in ['Administrador', 'Bodeguero']:
        return True
    raise PermissionDenied

@login_required
@user_passes_test(check_admin_or_bodeguero)
def producto_crud_view(request):
    return render(request, 'core/productos/producto_crud.html')

@login_required
@user_passes_test(check_admin_or_bodeguero)
def eliminar_producto_view(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return JsonResponse({'message': 'Producto eliminado exitosamente.'})
    return render(request, 'core/productos/eliminar_producto.html', {'producto': producto})

class CategoriaListView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoListView(generics.ListCreateAPIView):
    serializer_class = ProductoSerializer

    def get_queryset(self):
        queryset = Producto.objects.all()
        cat_id = self.request.query_params.get('cat', None)
        if cat_id and cat_id != 'all':
            queryset = queryset.filter(cat_id=cat_id)
        return queryset

    def perform_create(self, serializer):
        if 'imagen' not in self.request.FILES:
            serializer.save(imagen='productos/img_defect.png')
        else:
            serializer.save()

class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class PrecioProductoListView(generics.ListCreateAPIView):
    queryset = PrecioProducto.objects.all()
    serializer_class = PrecioProductoSerializer

class PrecioProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PrecioProducto.objects.all()
    serializer_class = PrecioProductoSerializer
