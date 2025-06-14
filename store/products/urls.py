from django.urls import path
from products.views import *

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/remove/<int:product_id>/', basket_remove, name='basket_remove'),
    path('basket/increment/<int:product_id>/', basket_increment, name='basket_increment'),
    path('basket/decrement/<int:product_id>/', basket_decrement, name='basket_decrement'),
]

