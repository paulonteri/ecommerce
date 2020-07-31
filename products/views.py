from django.http import Http404, HttpResponse
from django.shortcuts import render

from products.models import Item
from products.selectors.catagories import get_all_categories_with_subcategories
from products.selectors.items import get_item_full_detail


def product_detail(request, item_slug):
    """
    Renders the Product Detail Page
    """
    try:
        item_info = get_item_full_detail(item_slug)

        context = {
            'item': item_info["item"],
            "specifications": item_info["specifications"],
            "related_products": item_info["related_products"],
            "reviews": item_info["reviews"],
            "q_a": item_info["q_a"]
        }

        print(context)
    except Item.DoesNotExist:
        raise Http404("Items does not exist")

    return render(request, 'products/product_detail.html', context=context)


def index(request):
    return HttpResponse("Product")


def catalog(request):
    context = {
        "categories": get_all_categories_with_subcategories()
    }
    return render(request, 'categories/catalog.html', context=context)


def categories(request):
    return render(request, 'categories/index.html', {})


def subcategory(request):
    return render(request, 'categories/subcategory.html', {})
