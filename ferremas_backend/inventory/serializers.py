from rest_framework import serializers
from .models import Product, Comment, Category
from .utils import get_usd_value

class ProductSerializer(serializers.ModelSerializer):
    price_clp = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price_clp', 'image', 'stock']

    def get_price_clp(self, obj):
        usd_value = get_usd_value()
        if usd_value:
            return obj.price_clp * usd_value
        return None

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
