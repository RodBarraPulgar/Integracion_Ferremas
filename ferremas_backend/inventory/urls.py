from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CommentViewSet,product_list
from django.urls import path
from .views import product_list, get_usd_value, home,ProductViewSet, CommentViewSet, CategoryViewSet, product_list,category_list, product_detail

urlpatterns = [
     path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('usd-value/', get_usd_value, name='usd_value'),
    path('categories/', category_list, name='category_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    # path('payment/initiate/', initiate_payment, name='initiate_payment'),
    #path('payment/return/', payment_return, name='payment_return'),
]
router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'categories', CategoryViewSet)


