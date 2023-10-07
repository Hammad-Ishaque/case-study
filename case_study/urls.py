from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from sasta_ticket.views import GetOrdersByUserEmails
from sasta_ticket.views import ListAllUserEmails
from sasta_ticket.views import OrderDetailView
from sasta_ticket.views import OrderListCreateView
from sasta_ticket.views import UserDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('user/', UserDetailView.as_view(), name='user-detail'),
    path('all-user-emails/', ListAllUserEmails.as_view(), name='all-user-emails'),
    path('get-orders-by-emails/', GetOrdersByUserEmails.as_view(), name='get-orders-by-emails'),
]
