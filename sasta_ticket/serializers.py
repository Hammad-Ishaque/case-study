from rest_framework import serializers
from sasta_ticket.models import Order
from django.contrib.auth.models import User


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'order_number', 'total_amount', 'created_at', 'user')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number')


class UserEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')


class OrderEmailsSerializer(serializers.Serializer):
    emails = serializers.ListField(child=serializers.EmailField())
