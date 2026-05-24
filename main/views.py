from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home',
        'content': 'Welcome to the Home page',
        'list':['item1', 'item2', 'item3'],
        'dict': {'key1': 'value1', 'key2': 'value2'},
        'is_active': False
    }
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')
