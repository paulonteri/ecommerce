from products.selectors.brands import display_brands
from products.selectors.catagories import header_display_categories


def trending_brands_processor(request):
    brands = display_brands()
    return {'trending_brands': brands}


def header_categories_processor(request):
    header_categories = header_display_categories()
    return {'header_categories': header_categories}
