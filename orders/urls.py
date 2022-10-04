from django.urls import path
from . import views

app_name = 'orders'


urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('all_orders/', views.all_orders, name='all_orders'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('detail_order/<id>/', views.detail_order, name='detail_order'),
]