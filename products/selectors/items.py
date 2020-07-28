from products.models import Item

from django.db.models.query import QuerySet


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
    items = Item.objects.order_by("-time_last_edited")[:4]
    return items
