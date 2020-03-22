from rest_framework import serializers
# password hasher
from django.contrib.auth.hashers import make_password
# Models
from ..models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']


# class ChangePasswordSerializer(serializers.Serializer):
#     old_password = serializers.CharField(max_length=500)
#     new_password = serializers.CharField(max_length=500)
#     re_new_password = serializers.CharField(max_length=500)


class ChangePasswordSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('id', 'password')
        extra_kwargs = {'password': {'write_only': True}}


