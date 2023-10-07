from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from sasta_ticket.models import Order
from sasta_ticket.serializers import OrderSerializer
from sasta_ticket.serializers import OrderEmailsSerializer
from sasta_ticket.serializers import UserSerializer
from sasta_ticket.serializers import UserEmailSerializer


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListAllUserEmails(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserEmailSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class GetOrdersByUserEmails(APIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def post(self, request, format=None):
        serializer = OrderEmailsSerializer(data=request.data)
        if serializer.is_valid():
            emails = serializer.validated_data['emails']
            orders = Order.objects.filter(user__email__in=emails)
            order_serializer = OrderSerializer(orders, many=True)
            return Response(order_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
