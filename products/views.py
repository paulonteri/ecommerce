from django.shortcuts import render


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
