from django.shortcuts import render

from catalog.models import Product, Category


def home(request):
    game_list = Product.objects.all()
    context = {
        'object_list': game_list,
        'title': 'CityGames'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name} ({phone}): {message}')

    return render(request, 'catalog/contacts.html')


def game_detail(request, pk):
    context = {
        'object': Product.objects.get(id=pk)
    }
    return render(request, 'catalog/game_detail.html', context)


def genres(request):
    genres_list = Category.objects.all()
    context = {
        'object_list': genres_list
    }
    return render(request, 'catalog/genres_list.html', context)

