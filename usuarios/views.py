from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroForm, LoginForm, EditarUsuarioForm
from .models import Usuario, CategoriaUsuario
from django.db import IntegrityError
from rest_framework import generics
from .serializers import UsuarioSerializer, CategoriaUsuarioSerializer
from rest_framework import viewsets
from .models import Usuario, CategoriaUsuario
from .serializers import UsuarioSerializer, CategoriaUsuarioSerializer
from django.core.exceptions import PermissionDenied


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CategoriaUsuarioViewSet(viewsets.ModelViewSet):
    queryset = CategoriaUsuario.objects.all()
    serializer_class = CategoriaUsuarioSerializer

# Views for API endpoints
class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CategoriaUsuarioListCreateView(generics.ListCreateAPIView):
    queryset = CategoriaUsuario.objects.all()
    serializer_class = CategoriaUsuarioSerializer

class CategoriaUsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoriaUsuario.objects.all()
    serializer_class = CategoriaUsuarioSerializer

# Authentication and CRUD views
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inicio')
    else:
        form = LoginForm()
    return render(request, 'core/usuarios/login.html', {'form': form})

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            perfil_cliente = CategoriaUsuario.objects.get(nombrecategoria='Cliente')
            user.perfil_usuario = perfil_cliente
            user.save()
            login(request, user)
            messages.success(request, 'Registro exitoso.')
            return redirect('inicio')
    else:
        form = RegistroForm()
    return render(request, 'core/usuarios/registro.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('inicio')

@login_required
def crud_usuarios_view(request):
    if request.user.perfil_usuario.nombrecategoria != 'Administrador':
        raise PermissionDenied
    return render(request, 'core/usuarios/crud_usuarios.html')

@login_required
def editar_usuario_view(request, pk):
    if request.user.perfil_usuario.nombrecategoria != 'Administrador':
        raise PermissionDenied
    return render(request, 'core/usuarios/editar_usuario.html')

@login_required
def eliminar_usuario_view(request, pk):
    if request.user.perfil_usuario.nombrecategoria != 'Administrador':
        raise PermissionDenied
    return render(request, 'core/usuarios/eliminar_usuario.html')