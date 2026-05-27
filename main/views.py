from django.shortcuts import render
from goods.models import Categories


def index(request):
    categories = Categories.objects.all()

    context = {
        'title': 'Home - главная ',
        'content': 'Магазин мебели HOME',
        'categories': categories

    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - о нас',
        'content': 'O нас',
        'text_on_page': ' text about us and our company'

    }
    return render(request, 'main/about.html', context)
