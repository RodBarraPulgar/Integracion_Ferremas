from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Sale
from .serializers import SaleSerializer
from django.db.models.functions import TruncMonth
from rest_framework.views import APIView
from rest_framework.response import Response

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SalesByMonthView(APIView):
    def get(self, request):
        sales = Sale.objects.annotate(month=TruncMonth('date')).values('month').annotate(total_sales=Sum('total_amount')).order_by('month')
        data = {
            'months': [sale['month'].strftime('%Y-%m') for sale in sales],
            'total_sales': [sale['total_sales'] for sale in sales]
        }
        return Response(data)