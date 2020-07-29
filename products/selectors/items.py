from django.db.models import Q
from django.db.models.query import QuerySet

from django.core.validators import validate_slug

from products.models import Item, Brand, Category

from products.decorators import debugger_queries
from products.selectors.catagories import get_categories_ave_cost


def get_items() -> QuerySet:
    """
    A function that returns all items
    """
    items = Item.objects.all()
    return items


def get_homepage_items() -> dict:
    """
    The function that will return the featured items, brands to be displayed on the homepage.
    :returns: items: A dict containing trending items & brands.
    """
    # ITEMS
    items = Item.objects.all().order_by("-time_last_edited")[:12].only(
        "title", "price", "discount_price", "slug", "description",
        "image", "brand__title", "sub_category__title")
    # Top selling
    top_selling = True
    for obj in items:
        # logic for top selling items will be added here...
        obj.top_selling = top_selling
        top_selling = not top_selling

    # CATEGORIES
    categories = get_categories_ave_cost(Category.objects.all().order_by("-time_last_edited"))

    data = {
        "trending_items": items,
        "trending_categories": categories
    }

    return data


def debugger_get_homepage_items():
    """Run debugger queries for get_homepage_items function."""
    return debugger_queries(get_homepage_items)()


def get_item_detail(item_slug: str) -> Item:
    """
    Gets a particular Item info from it's slug
    :param item_slug: products.models.Item.slug
    :returns: products.models.Item
    """
    validate_slug(item_slug)

    item = Item.objects.get(slug__exact=item_slug)

    return item


def get_item_related_products(item_slug: str) -> QuerySet:
    """
    Gets a particular Item info from it's slug
    :param item_slug: products.models.Item.slug
    :returns: Queryset with item's related_products
    """

    validate_slug(item_slug)

    # TODO: Implement Logic
    items = Item.objects.order_by("-time_last_edited") \
                .filter(~Q(slug=item_slug))[:15] \
        .only(
        "title", "price", "discount_price", "slug", "description",
        "image", "brand__title", "sub_category__title")
    return items


def get_item_full_detail(item_slug: str) -> dict:
    """
    Gets a particular Item info from it's slug
    :param item_slug: products.models.Item.slug
    :returns: an Item with all related info including scpecifications, reviews, related_products
    """
    validate_slug(item_slug)

    item = get_item_detail(item_slug)
    item.sub_category_title = item.sub_category.title.capitalize()
    item.brand_title = item.brand.title.capitalize()
    item.brand_image_url = item.brand.image.url
    item.sub_category_category_title = item.sub_category.category.title.capitalize()

    specifications = {}
    related_products = get_item_related_products(item_slug)
    reviews = []
    q_a = []

    item_info = {
        "item": item,
        "specifications": specifications,
        "related_products": related_products,
        "reviews": reviews,
        "q_a": q_a
    }

    return item_info


def debugger_get_item_full_detail(slug):
    """Run debugger queries for get_item_full_detail function."""
    return debugger_queries(get_item_full_detail)(slug)
