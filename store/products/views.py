from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from products.models import *
from django.contrib.auth.decorators import login_required

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


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(user=request.user, product=product)

    if not basket.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = basket.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def basket_remove(request, product_id):
    basket = get_object_or_404(Basket, id=product_id, user=request.user)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



def basket_increment(request, basket_id):
    basket_item = get_object_or_404(Basket, id=basket_id, user=request.user)
    basket_item.quantity += 1
    basket_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



def basket_decrement(request, basket_id):
    basket_item = get_object_or_404(Basket, id=basket_id, user=request.user)
    if basket_item.quantity > 1:
        basket_item.quantity -= 1
        basket_item.save()
    else:
        basket_item.delete()  # Если стало 0, удалим
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))