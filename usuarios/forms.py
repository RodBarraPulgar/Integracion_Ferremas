from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'nombre', 'apellido', 'correo', 'rut', 'direccion', 'telefono', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass

class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'correo', 'rut', 'direccion', 'telefono', 'perfil_usuario']
