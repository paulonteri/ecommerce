from django.shortcuts import render

from products.selectors.items import get_homepage_items


def index(request):

    display_items = get_homepage_items()

    context = {'display_items': display_items}

    return render(request, 'home/index.html', context=context)
