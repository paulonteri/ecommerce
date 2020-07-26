from os import listdir, path

from django.conf import settings
from django.core.files import File
from termcolor import colored

from products.models import Brand, Category, SubCategory

# TODO: This is not flexible enough. Will improve
# Paths
base_dir = settings.BASE_DIR
images_dir = base_dir + "/media/images/static"
brands_dir = images_dir + "/brands"
categories_dir = images_dir + "/catalog"
# Values
# [sub_category, category]
categories_vars = ['tablets', 'consoles', 'smartphones', 'computers', 'phones',
                   'photo', 'tv', 'games', 'laptops', 'cameras', 'watches']
subcategories_vars_one = ['iPad', 'Xbox', 'Android', 'Desktop', 'Feature Phone',
                          'Lenses', 'Smart TV', 'PS4', 'MacBook', 'DSLR', 'Wrist']


class Seed:

    def save_brands(self):
        # Seed Brands
        files = listdir(brands_dir)
        count = 0

        for i in files:
            file_path = brands_dir + "/" + i

            try:
                file_name = path.splitext(i)[0]

                with open(file_path, "rb") as f:
                    data = File(f)
                    obj = Brand(title=file_name.capitalize())
                    obj.image.save(i, data, save=True)

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
                    data = File(f)
                    obj = Category(title=file_name)
                    obj.image.save(i, data, save=True)

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
        length = len(subcategories_vars_one)
        q = 0

        while q < length:
            q += 1
            try:
                obj = SubCategory(category=cat.get(
                    title=categories_vars[q]), title=subcategories_vars_one[q])
                obj.save()
            except Exception as e:
                print("Error: \n" + str(e))

            else:
                count += 1

        if count > 0:
            print(colored("Successfully added " + str(count) +
                          " SubCategories to the database...", "green"))
        else:
            print(colored("No SubCategories were added to the database...", "red"))

    def save_all(self):
        self.save_brands()
        self.save_categories()
        self.save_subcategories()
