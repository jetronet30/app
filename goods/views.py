from django.shortcuts import render

from . import goods_list


def catalog(request):
    context = {
        'title': 'Home - Каталог',
        'goods': goods_list.goods
        }
    return render(request, 'goods/catalog.html', context)


 
def product(request):
    return render(request, 'goods/product.html')
