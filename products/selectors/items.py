from django.db.models.query import QuerySet

from products.models import Item


def get_items() -> QuerySet:
    """
    A function that returns all items
    """
    items = Item.objects.all()
    return items


def get_homepage_items() -> QuerySet:
    """
    The function that will return the featured items tobe displayed on the homepage.

    Parameters:
        None

    Returns:
        items: A Queryset containing items.
    """
    items = Item.objects.order_by("-time_last_edited")[:4].only(
        "title", "price", "discount_price", "slug", "description",
        "image", "brand__title", "sub_category__title")

    # Top selling
    top_selling = True
    for obj in items:
        # logic for top selling items will be added here...
        obj.top_selling = top_selling
        top_selling = not top_selling

    return items
