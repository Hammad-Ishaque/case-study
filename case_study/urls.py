"""
URL configuration for case_study project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sasta_ticket.views import GetOrdersByUserEmails
from sasta_ticket.views import ListAllUserEmails
from sasta_ticket.views import OrderDetailView
from sasta_ticket.views import OrderListCreateView
from sasta_ticket.views import UserDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('user/', UserDetailView.as_view(), name='user-detail'),
    path('all-user-emails/', ListAllUserEmails.as_view(), name='all-user-emails'),
    path('get-orders-by-emails/', GetOrdersByUserEmails.as_view(), name='get-orders-by-emails'),
]
