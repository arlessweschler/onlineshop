from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('discount_managment/', views.discount_managment, name='discount_managment'),
    path('<category_slug>/', views.product_list, name='product_list_by_category'),
    path('product_detail/<id>/<slug>/', views.product_detail, name='product_detail'),
    path('product_detail/<id>/<slug>/review/', views.product_review, name='product_review'),
    path('product_detail/<id>/<slug>/review_and_rating/', views.review_and_rating, name='review_and_rating'),
    path('shipping', views.shipping, name='shipping'),
    path('contacts', views.contacts, name='contacts'),
    path('payment', views.payment, name='payment'),
    path('discounts', views.discounts, name='discounts'),

]