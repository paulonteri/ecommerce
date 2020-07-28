from django.shortcuts import render

from products.selectors.items import get_homepage_items


def index(request):
    data = get_homepage_items()

    context = {
        'display_items': data["trending_items"],
        "brands": data["trending_brands"]
    }

    return render(request, 'home/index.html', context=context)
