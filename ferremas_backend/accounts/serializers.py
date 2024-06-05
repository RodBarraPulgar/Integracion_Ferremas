from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'phone', 'address', 'rut']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            phone=validated_data['phone'],
            address=validated_data['address'],
            rut=validated_data['rut']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
