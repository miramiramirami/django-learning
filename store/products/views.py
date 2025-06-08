from django.shortcuts import render
from products.models import *

#funcs = controllers

def index(request):
    context = {'title': 'store',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': Category.objects.all(),

    }
    return render(request, 'products/products.html', context)

