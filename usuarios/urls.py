from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/usuarios', views.UsuarioViewSet)
router.register(r'api/categorias', views.CategoriaUsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('crud/', views.crud_usuarios_view, name='crud'),
    path('crud/editar/<int:pk>/', views.editar_usuario_view, name='editar-usuario'),
    path('crud/eliminar/<int:pk>/', views.eliminar_usuario_view, name='eliminar-usuario'),
    path('registro/', views.registro_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
