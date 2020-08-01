from random import randint

from django.conf import settings
from django.db.models import QuerySet

from products.models import Category, Item, SubCategory, Brand


def get_all_categories_with_subcategories() -> list:
    """
    All categories, each with all it's categories
    :return: All categories, each with all it's categories
    """
    categories = Category.objects.values("id", "title", "image"  # ,"slug"
                                         )
    sub_categories = SubCategory.objects.values("title", "category_id"  # ,"slug"
                                                )
    cats = []
    for foo in categories:
        foo["image"] = settings.MEDIA_URL + foo["image"]
        foo["sub_categories"] = [
            x for x in sub_categories if x['category_id'] == foo["id"]]
        if len(foo["sub_categories"]) > 0:
            cats.append(foo)

    return cats


def get_categories_ave_cost(categories: QuerySet) -> QuerySet:
    """
    :param categories: products.models.Category Queryset
    :return: Average cost of each category
    """
    items = Item.objects.all()
    price = 0
    for obj in categories:
        y = items.filter(sub_category__category_id__exact=obj.id)
        if len(y) > 0:
            total_costs = 0
            for i in y:
                total_costs += i.price
            price = total_costs / len(y)
        else:
            price = randint(299, 99999)
        obj.average_cost = price
    return categories


def header_display_categories() -> set:
    """
    The Categories and Subcategories displayed on the Header
    :return: The Categories and Subcategories displayed on the Header
    """
    categories = Category.objects.only("id", "title", "image",  # "slug"
                                       )
    wanted_categories = set()
    for value in categories:
        value.the_subcategories = value.subcategory_set.all()
        if len(value.the_subcategories) > 0 and len(wanted_categories) <= 4:
            wanted_categories.add(value)

    return wanted_categories


def get_category_detail() -> dict:
    """
    Get a category's details for display on category page
    """
    category = Category.objects.all().values("id", 'title',
                                             # ,'category__slug'
                                             )[6]
    # category = Category.objects.get(slug=slug)

    subcategories = SubCategory.objects.filter(category=category["id"]).values('id', 'title'  # ,'slug'
                                                                               )
    subcategory_ids = []
    for bar in subcategories:
        subcategory_ids.append(bar["id"])
        del bar["id"]

    items = Item.objects.filter(sub_category__in=subcategory_ids).values('title', 'price', 'discount_price', 'image',
                                                                         'brand_id', 'slug', 'sub_category__title')
    brand_ids = []
    for item in items:
        item["image"] = settings.MEDIA_URL + item["image"]
        brand_ids.append(item["brand_id"])
    brands = Brand.objects.filter(pk__in=brand_ids).values("title"  # ,"slug"
                                                           )

    category["subcategories"] = list(subcategories)
    category["items"] = list(items)
    category["brands"] = list(brands)

    del category["id"]

    return category
