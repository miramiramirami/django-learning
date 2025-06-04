from django.shortcuts import render

#funcs = controllers

def index(request):
    context = {'title': 'store',
               'username': 'nickname',
    }
    return render(request, 'products/index.html', context)


def products(request):
    return render(request, 'products/products.html')

