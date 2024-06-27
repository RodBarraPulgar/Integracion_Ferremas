from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/ventas', views.VentaViewSet)
router.register(r'api/detalles_venta', views.DetalleVentaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('crud/', views.crud_ventas_view, name='crud_ventas'),
    path('crud/detalle/<int:pk>/', views.detalle_venta_view, name='detalle_venta'),
    path('crud/eliminar/<int:pk>/', views.eliminar_venta_view, name='eliminar_venta'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('pago/iniciar/', views.iniciar_pago, name='iniciar_pago'),
    path('pago/exito/', views.exito_pago, name='exito_pago'),
    path('ventas/analisis/', views.analisis_ventas_view, name='analisis_ventas'),
    path('api/ventas/', views.ventas_api, name='ventas_api'),
    path('api/ventas/<int:id>/', views.ventas_delete, name='ventas_delete'),
]
