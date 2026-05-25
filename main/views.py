from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home - главная ',
        'content': 'Магазин мебели HOME'

    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - о нас',
        'content': 'O нас',
        'text_on_page': ' text about us and our company'

    }
    return render(request, 'main/about.html', context)
