from django.db.models import QuerySet

from products.models import Brand


def display_brands() -> QuerySet:
    """
    Function to return the brands that will be advertised throughout the site
    :return: QuerySet of products.models.Brand
    """
    brands = Brand.objects.all().order_by("-time_last_edited")[:15]
    return brands
