from django.urls import path

from .views import products, product

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('product/<int:pk>', product, name='product'),
]
