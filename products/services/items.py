from accounts.models import User
from products.models import Item, SubCategory, Brand
from django.core.files.images import ImageFile
from os import path


def save_products(title, price, sub_category_id, brand_id, description, slug, image, user_id, discount_price=None):
    # Save product only without varaiations e.t.c

    if not type(image) == ImageFile:
        raise Exception("Please submit an image")

    prod = None

    try:
        brand = Brand.objects.get(pk=brand_id)
        sub_category = SubCategory.objects.get(pk=sub_category_id)
        usr = User.objects.get(pk=user_id)

        item = Item(title=title, description=description, slug=slug,
                    price=price, discount_price=discount_price, brand=brand, sub_category=sub_category, last_edited_by=usr)
        item.image.save(path.basename(image.name), image, save=True)
        prod = item
    except Exception as e:
        raise e
    else:
        return prod
