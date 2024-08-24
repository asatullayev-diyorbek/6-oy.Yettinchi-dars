from django.urls import path
from .views import category, product, customer

urlpatterns = [
    path('', category, name='category'),
    path('product/', product, name='product'),
    path('customer/', customer, name='customer'),
]
