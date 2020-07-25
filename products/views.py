from django.shortcuts import render


def index(request):
    return render(request, 'products/index.html', {})


def catalog(request):
    return render(request, 'catalog/index.html', {})


def categories(request):
    return render(request, 'categories/index.html', {})
