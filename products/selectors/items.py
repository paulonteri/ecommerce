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
    :returns: items: A Queryset containing items.
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


def get_item_detail(item_slug: str) -> Item:
    """
    Gets a particular Item info from it's slug
    :param item_slug: products.models.Item.slug
    :returns: products.models.Item
    """
    item = Item.objects.get(slug__exact=item_slug)

    return item


def get_item_full_detail(item_slug: str) -> dict:
    """
    Gets a particular Item info from it's slug
    :param item_slug: products.models.Item.slug
    :returns: an Item with all related info including scpecifications, reviews, accessories
    """
    item = get_item_detail(item_slug)
    item.sub_category_title = item.sub_category.title.capitalize()
    item.brand_title = item.brand.title.capitalize()
    item.brand_image_url = item.brand.image.url
    item.sub_category_category_title = item.sub_category.category.title.capitalize()

    specifications = {}
    accessories = []
    reviews = []
    q_a = []

    item_info = {
        "item": item,
        "specifications": specifications,
        "accessories": accessories,
        "reviews": reviews,
        "q_a": q_a
    }

    return item_info
