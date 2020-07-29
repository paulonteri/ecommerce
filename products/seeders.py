from os import listdir, path
from random import randint

from django.conf import settings
from django.core.files.images import ImageFile
from termcolor import colored

from accounts.models import User
from products.models import Brand, Category, SubCategory
from products.services.items import save_products

# TODO: This is not flexible enough. Will improve
# Paths
base_dir = settings.BASE_DIR
images_dir = base_dir + "/media/images"
products_dir = images_dir + "/seed_data/products"
brands_dir = images_dir + "/static/brands"
categories_dir = images_dir + "/static/catalog"
# Values
# category
category_vars = ['tablets', 'consoles', 'smartphones', 'computers', 'phones',
                 'photo', 'tv', 'games', 'laptops', 'cameras', 'watches']
# sub category
subcategory_vars_one = ['iPad', 'Xbox', 'Android', 'Desktop', 'Feature Phone',
                        'Lenses', 'Smart TV', 'Play Station', 'MacBook', 'DSLR', 'Wrist']
# brands
brands_vars_one = ["Apple", "Microsoft", "Samsung", "Hp", "Lg", "Canon", "Asus", "Sony", "Apple", "Canon", "Samsung"]
# product
product_vars_one = ["iPad_Pro", "XBox_360", "Samsung_Galaxy_Note_10", "HP_Omen", "LG_Feature_Phone",
                    "Canon_Lens", "Asus_TV", "Play_Station_4", "MacBook_Air", "Canon_Camera", "Samsung_Gear"]


class Seed:
    user = User.objects.all()[0]

    def save_brands(self):
        # Seed Brands
        files = listdir(brands_dir)
        count = 0

        for i in files:
            file_path = brands_dir + "/" + i

            try:
                file_name = path.splitext(i)[0]

                with open(file_path, "rb") as f:
                    img = ImageFile(f)
                    obj = Brand(title=file_name.capitalize())
                    obj.image.save(i, img, save=True)

            except Exception as e:
                print("Error: \n" + str(e))

            else:
                count += 1

        if count > 0:
            print(colored("Successfully added " + str(count) +
                          " Brands to the database...", "green"))
        else:
            print(colored("No Brands were added to the database...", "red"))

    def save_categories(self):
        # Seed Categories
        files = listdir(categories_dir)
        count = 0

        for i in files:
            file_path = categories_dir + "/" + i

            try:
                file_name = path.splitext(i)[0]

                with open(file_path, "rb") as f:
                    img = ImageFile(f)
                    obj = Category(title=file_name)
                    obj.image.save(i, img, save=True)

            except Exception as e:
                print("Error: \n" + str(e))

            else:
                count += 1

        if count > 0:
            print(colored("Successfully added " + str(count) +
                          " Categories to the database...", "green"))
        else:
            print(colored("No Categories were added to the database...", "red"))

    def save_subcategories(self):
        # Seed SubCategories
        count = 0
        cat = Category.objects.all()
        length = len(subcategory_vars_one)
        q = 0

        while q < length:
            sub_cat_name = subcategory_vars_one[q]
            try:
                obj = SubCategory(category=cat.get(
                    title=category_vars[q]), title=subcategory_vars_one[q])
                obj.save()
            except Exception as e:
                print("Error: \n" + str(e))

            else:
                count += 1
            finally:
                q += 1

        if count > 0:
            print(colored("Successfully added " + str(count) +
                          " SubCategories to the database...", "green"))
        else:
            print(colored("No SubCategories were added to the database...", "red"))

    def save_products(self):
        # Seed Products
        count = 0
        length = len(product_vars_one)
        q = 0

        while q < length:

            prod_name = product_vars_one[q]
            file_path = products_dir + "/" + str(prod_name) + ".jpeg"

            all_sub_cat = SubCategory.objects.all()
            all_brands = Brand.objects.all()

            try:
                sub_cat = all_sub_cat.get(
                    title__exact=subcategory_vars_one[q].lower())
                brand = all_brands.get(title__exact=brands_vars_one[q])
                #
                with open(file_path, "rb") as f:
                    img = ImageFile(f)
                    save_products(title=prod_name.replace("_", " "), price=randint(9999, 999999),
                                  sub_category_id=sub_cat.id, brand_id=brand.id,
                                  description=prod_name.replace("_", " ") + "...", slug='_' + prod_name, image=img,
                                  user_id=self.user.id)
            except Exception as e:
                print("Error: \n" + str(e))

            else:
                count += 1
            finally:
                q += 1

        if count > 0:
            print(colored("Successfully added " + str(count) +
                          " Products to the database...", "green"))
        else:
            print(colored("No Products were added to the database...", "red"))

    def save_all(self):
        self.save_brands()
        self.save_categories()
        self.save_subcategories()
        self.save_products()
