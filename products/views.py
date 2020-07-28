from django.shortcuts import render

from products.selectors.items import get_item_full_detail


def product_detail(request, item_slug):
    """
    Renders the Product Detail Page
    """
    item_info = get_item_full_detail(item_slug)

    context = {
        'item': item_info["item"],
        "speciications": item_info["specifications"],
        "accessories": item_info["accessories"],
        "reviews": item_info["reviews"],
        "q_a": item_info["q_a"]
    }

    print(context)
    return render(request, 'products/product_detail.html', context=context)


def index(request):
    return render(request, 'products/index.html', {})


def catalog(request):
    return render(request, 'catalog/index.html', {})


def categories(request):
    return render(request, 'categories/index.html', {})


def subcategory(request):
    return render(request, 'categories/subcategory.html', {})

# def detail(request, poll_id):
#     try:
#         p = Poll.objects.get(pk=poll_id)
#     except Poll.DoesNotExist:
#         raise Http404("Poll does not exist")
#     return render(request, 'polls/detail.html', {'poll': p})
