from products.selectors.brands import display_brands


def trending_brands_processor(request):
    brands = display_brands()
    return {'trending_brands': brands}
