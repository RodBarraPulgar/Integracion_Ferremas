from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/categorias/', views.CategoriaListView.as_view(), name='categoria-list'),
    path('api/categorias/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria-detail'),
    path('api/productos/', views.ProductoListView.as_view(), name='producto-list'),
    path('api/productos/<int:pk>/', views.ProductoDetailView.as_view(), name='producto-detail'),
    path('crud/producto_crud/', views.producto_crud_view, name='producto_crud'),
    path('api/precios/', views.PrecioProductoListView.as_view(), name='precio-producto-list'),
    path('api/precios/<int:pk>/', views.PrecioProductoDetailView.as_view(), name='precio-producto-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)