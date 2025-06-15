from django.urls import path
from products.views import *

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:category_id>', products, name='category'),
    path('page/<int:page_number>', products, name='paginator'),
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/remove/<int:product_id>/', basket_remove, name='basket_remove'),
    path('basket/increment/<int:product_id>/', basket_increment, name='basket_increment'),
    path('basket/decrement/<int:product_id>/', basket_decrement, name='basket_decrement'),
]

