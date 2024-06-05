from django.contrib import admin
from django.urls import path, include
from inventory.views import home
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('inventory.urls')),
    path('', home, name='home'),
    path('api/', include('accounts.urls')),
    
    path('api/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('accounts.urls')),
    path('api/', include('sales.urls')),
    path('inventory/', include('inventory.urls')),
]