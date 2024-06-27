from django.views.generic import TemplateView
from django.shortcuts import render
from django.core.exceptions import PermissionDenied

class InicioView(TemplateView):
    template_name = 'core/inicio.html'

def error_403_view(request, exception):
    return render(request, 'core/403.html', status=403)