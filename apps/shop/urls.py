from django.contrib import admin
from django.urls import path, include

from apps.shop.views import MainView, CreateOrderView, TestView

urlpatterns = [
    path('', MainView.as_view(), name='list'),
    path('order/<int:pk>', CreateOrderView.as_view(), name='order'),
    path('test/', TestView.as_view(), name='test'),

]