from django.db import models
from django.contrib.auth.models import AbstractUser

class CategoriaUsuario(models.Model):
    nombrecategoria = models.CharField(max_length=50, unique=True, verbose_name='Nombre de la categoría')

    def __str__(self):
        return self.nombrecategoria

class Usuario(AbstractUser):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    correo = models.EmailField(unique=True, verbose_name='Correo')
    rut = models.CharField(max_length=12, unique=True, verbose_name='RUT')
    direccion = models.CharField(max_length=255, verbose_name='Dirección')
    telefono = models.CharField(max_length=15, verbose_name='Teléfono')
    perfil_usuario = models.ForeignKey(CategoriaUsuario, on_delete=models.CASCADE, verbose_name='Perfil de Usuario')

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
    def save(self, *args, **kwargs):
        if self.is_superuser and not self.perfil_usuario_id:
            self.perfil_usuario, _ = CategoriaUsuario.objects.get_or_create(nombrecategoria='Administrador')
        super().save(*args, **kwargs)
