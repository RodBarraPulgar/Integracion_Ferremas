from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SaleViewSet
from .views import SalesByMonthView

router = DefaultRouter()
router.register(r'sales', SaleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('sales_by_month/', SalesByMonthView.as_view(), name='sales_by_month'),
]
