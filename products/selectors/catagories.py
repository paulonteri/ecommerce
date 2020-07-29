from random import randint

from django.db.models import QuerySet

from products.models import Category, Item


def get_categories_ave_cost(categories: QuerySet) -> QuerySet:
    """
    :param categories: products.models.Category Queryset
    :return: Average cost of category
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
