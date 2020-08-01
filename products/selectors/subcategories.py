from django.conf import settings

from products.models import SubCategory, Item, Brand


def get_subcategory_detail() -> dict:
    """
    Get a subcategory's details for display on subcategory page
    """
    subcategory = SubCategory.objects.all().values("id", 'title', 'category__title')[5]
    # subcategory = SubCategory.objects.get(slug=slug)
    items = Item.objects.filter(sub_category=subcategory["id"]).values('title', 'price', 'discount_price', 'image',
                                                                       'brand_id', 'slug')
    brand_ids = []
    for foo in items:
        foo["image"] = settings.MEDIA_URL + foo["image"]
        brand_ids.append(foo["brand_id"])
    brands = Brand.objects.filter(pk__in=brand_ids).values("title"  # ,"slug"
                                                           )

    subcategory["items"] = list(items)
    subcategory["brands"] = list(brands)

    return subcategory
