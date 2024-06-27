from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Venta, DetalleVenta
from productos.models import Producto
from .serializers import VentaSerializer, DetalleVentaSerializer
from rest_framework import viewsets
from django.urls import reverse
from transbank.webpay.webpay_plus.transaction import Transaction, WebpayOptions
from transbank.common.integration_type import IntegrationType
import uuid
import json
from django.utils import timezone
from django.db.models import Sum, Q
from django.utils.dateparse import parse_date
from django.utils.timezone import make_aware
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def ventas_api(request):
    keyword = request.GET.get('keyword', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')

    ventas = Venta.objects.all()

    if keyword:
        ventas = ventas.filter(Q(usuario__username__icontains=keyword) | Q(buy_order__icontains=keyword))

    if start_date and end_date:
        try:
            start_date = make_aware(datetime.strptime(start_date, '%Y-%m-%d'))
            end_date = make_aware(datetime.strptime(end_date, '%Y-%m-%d'))
            ventas = ventas.filter(transaction_date__range=[start_date, end_date])
        except ValueError as e:
            print(f"Error parsing dates: {e}")

    if not keyword and not (start_date and end_date):
        ventas = ventas.order_by('-transaction_date')[:30]

    ventas_list = [
        {
            'id': venta.id,
            'usuario': str(venta.usuario),
            'buy_order': venta.buy_order,
            'amount': float(venta.amount),
            'transaction_date': venta.transaction_date.isoformat(),
        }
        for venta in ventas
    ]

    return JsonResponse(ventas_list, safe=False)

@csrf_exempt
def ventas_delete(request, id):
    if request.method == 'DELETE':
        venta = get_object_or_404(Venta, id=id)
        venta.delete()
        return JsonResponse({'message': 'Venta eliminada correctamente.'})
    return JsonResponse({'error': 'Método no permitido.'}, status=405)

@login_required
@user_passes_test(lambda u: u.perfil_usuario.nombrecategoria in ['Administrador', 'Contador'])
def analisis_ventas_view(request):
    today = timezone.now()
    start_date_str = request.GET.get('start_date', today.replace(day=1).date().isoformat())
    end_date_str = request.GET.get('end_date', today.date().isoformat())

    start_date = parse_date(start_date_str)
    end_date = parse_date(end_date_str)

    ventas = Venta.objects.filter(transaction_date__range=[start_date, end_date])
    ventas_por_dia = ventas.annotate(day=TruncDay('transaction_date')).values('day').annotate(total=Sum('amount')).order_by('day')

    data = {str(day['day']): float(day['total']) for day in ventas_por_dia}

    context = {
        'ventas_data': json.dumps(data),
        'start_date': start_date_str,
        'end_date': end_date_str,
    }
    return render(request, 'core/ventas/analisis_ventas.html', context)

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class DetalleVentaViewSet(viewsets.ModelViewSet):
    queryset = DetalleVenta.objects.all()
    serializer_class = DetalleVentaSerializer

@login_required
@user_passes_test(lambda u: u.perfil_usuario.nombrecategoria in ['Administrador', 'Contador'])
def crud_ventas_view(request):
    return render(request, 'core/ventas/crud_ventas.html')

@login_required
@user_passes_test(lambda u: u.perfil_usuario.nombrecategoria in ['Administrador', 'Contador'])
def detalle_venta_view(request, pk):
    venta = get_object_or_404(Venta.objects.select_related('usuario'), pk=pk)
    detalles = DetalleVenta.objects.filter(venta=venta)
    return render(request, 'core/ventas/detalle_venta.html', {'venta': venta, 'detalles': detalles})

@login_required
@user_passes_test(lambda u: u.perfil_usuario.nombrecategoria in ['Administrador', 'Contador'])
def eliminar_venta_view(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    return render(request, 'core/ventas/eliminar_venta.html', {'venta': venta})

@login_required
def checkout_view(request):
    return render(request, 'core/checkout.html')

def exito_pago(request):
    token = request.GET.get('token_ws')
    if not token:
        return render(request, 'core/error.html', {'message': 'Token no proporcionado'})

    options = WebpayOptions("597055555532", "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C", IntegrationType.TEST)
    response = Transaction(options).commit(token)
    
    buy_order = response.get('buy_order')
    amount = response.get('amount')
    transaction_date = response.get('transaction_date')
    detalles = request.session.get('cart', [])

    venta = Venta.objects.create(
        usuario=request.user,
        buy_order=buy_order,
        amount=amount,
        transaction_date=transaction_date,
        detalles=detalles
    )

    for item in detalles:
        producto = Producto.objects.get(id=item['id'])
        cantidad = item['quantity']
        precio_unitario = item['price']

        DetalleVenta.objects.create(
            venta=venta,
            producto=producto,
            cantidad=cantidad,
            precio_unitario=precio_unitario
        )

        producto.stock -= cantidad
        producto.save()

    request.session['cart'] = []

    return render(request, 'core/exito_pago.html', {'response': response})

def iniciar_pago(request):
    if request.method == 'POST':
        buy_order = str(uuid.uuid4())[:26]
        session_id = str(uuid.uuid4())
        amount = request.POST.get('amount')
        cart = json.loads(request.POST.get('cart'))
        return_url = request.build_absolute_uri(reverse('exito_pago'))

        request.session['cart'] = cart

        options = WebpayOptions("597055555532", "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C", IntegrationType.TEST)
        response = Transaction(options).create(buy_order, session_id, amount, return_url)

        return render(request, 'core/iniciar_pago.html', {
            'url': response['url'],
            'token': response['token'],
            'buy_order': buy_order,
            'amount': amount,
        })
    else:
        return redirect('checkout')