from django.shortcuts import render

#funcs = controllers

def index(request):
    context = {'title': 'store',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': [
            {'image': 'static/vendor/img/products/Adidas-hoodie.png',
            'name': 'Худи черного цвета с монограммами adidas Originals',
             'price': 6090,
             'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
            },
            {'image': 'static/vendor/img/products/Adidas-hoodie.png',
             'name': 'Худи черного цвета с монограммами adidas Originals',
             'price': 6090,
             'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
             },
            {'image': 'static/vendor/img/products/Adidas-hoodie.png',
             'name': 'Худи черного цвета с монограммами adidas Originals',
             'price': 6090,
             'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
             },{'image': 'static/vendor/img/products/Adidas-hoodie.png',
            'name': 'Худи черного цвета с монограммами adidas Originals',
             'price': 6090,
             'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это обраfffffffffз жизни.',
            }
        ]

    }
    return render(request, 'products/products.html', context)

