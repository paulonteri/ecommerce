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
images_dir = base_dir + "/seed_data/images"
products_dir = images_dir + "/products"
brands_dir = images_dir + "/brands"
categories_dir = images_dir + "/categories"
# Values

# brands
brands = ["Apple", "Microsoft", "Samsung", "Hp", "Lg",
          "Canon", "Asus", "Sony", "Samsung", "Dell", "Intel", "Lenovo"]

category_vars = ['tablets', 'consoles', 'computers',
                 'phones', 'photo', 'tv', 'games', 'watches']
#
brand_vars_one = ["Apple", "Microsoft", "Hp", "Lg",
                  "Canon", "Asus", "Sony", "Samsung"]

subcategory_vars_one = ['iPad', 'Xbox', 'Desktop', 'Feature Phone',
                        'Lenses', 'Smart TV', 'Play Station', 'Smart Watch']

product_vars_one = ["iPad_Pro", "XBox_360", "HP_Omen", "LG_Feature_Phone",
                    "Canon_Lens", "Asus_TV", "The_Witcher", "Samsung_Gear"]
#
brand_vars_two = ["Microsoft", "Sony", "Apple", "Samsung",
                  "Canon", "Lg", "Sony", "Apple"]

subcategory_vars_two = ["Surface", "Play Station", 'MacBook',
                        "Android", 'DSLR Camera', "LED TV", "PC", "Luxury"]

product_vars_two = ["Microsoft_Surface", "Play_Station_4", "MacBook_Air", "Samsung_Galaxy_Note_10",
                    "Canon_Camera", "LG_LED_TV", "GTA_V", "Apple_Watch_3"]
#
brand_vars_three = ["Intel", "Dell", "Apple", "Apple",
                    "Sony", "Lenovo", "Sony", "Asus"]

subcategory_vars_three = ["Intel Notebook", "Alienware", 'MacBook', "iPhone",
                          'CyberShot Camera', "4K TV", "XBox", "Health"]

product_vars_three = ["Intel_Tablet", "Dell_Alienware", "MacBook_Pro", "iPhone_11",
                      "Sony_CyberShot_Camera", "Lenovo_4K_TV", "Snow_Runner", "Asus_Vivo_Watch.jpeg"]


# # # # # #

class Seed:
    user = User.objects.all()
    sub_cat_count = 0
    prod_count = 0

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

    def _save_subcategories(self, sub_categ, categ):
        # Seed SubCategories
        cat = Category.objects.all()
        length = len(sub_categ)
        q = 0

        while q < length:
            try:
                obj = SubCategory(category=cat.get(
                    title=categ[q]), title=sub_categ[q])
                obj.save()
            except Exception as e:
                print("Error: \n" + str(e))
                print(q)

            else:
                self.sub_cat_count += 1
            finally:
                q += 1

    def save_subcategories(self):
        self._save_subcategories(subcategory_vars_one, category_vars)
        self._save_subcategories(subcategory_vars_two, category_vars)
        self._save_subcategories(subcategory_vars_three, category_vars)

        if self.sub_cat_count > 0:
            print(colored("Successfully added " + str(self.sub_cat_count) +
                          " SubCategories to the database...", "green"))
        else:
            print(colored("No SubCategories were added to the database...", "red"))

    def _save_products(self, prod, sub_categ, br):
        # Seed Products
        length = len(prod)
        q = 0

        while q < length:
            prod_name = prod[q]
            file_path = products_dir + "/" + str(prod_name) + ".jpeg"
            all_sub_cat = SubCategory.objects.all()
            all_brands = Brand.objects.all()

            try:
                sub_cat = all_sub_cat.get(
                    title__exact=sub_categ[q].lower())
                brand = all_brands.get(title__exact=br[q])
                #
                with open(file_path, "rb") as f:
                    img = ImageFile(f)
                    save_products(title=prod_name.replace("_", " "), price=randint(9999, 999999),
                                  sub_category_id=sub_cat.id, brand_id=brand.id,
                                  description=prod_name.replace("_", " ") + "...", slug='_' + prod_name, image=img,
                                  user_id=self.user[0].id)
            except Exception as e:
                print("Error: \n" + str(e))
                print(q)
            else:
                self.prod_count += 1
            finally:
                q += 1

    def save_products(self):
        self._save_products(
            product_vars_one, subcategory_vars_one, brand_vars_one)
        self._save_products(
            product_vars_two, subcategory_vars_two, brand_vars_two)
        self._save_products(
            product_vars_three, subcategory_vars_two, brand_vars_three)

        if self.prod_count > 0:
            print(colored("Successfully added " + str(self.prod_count) +
                          " Products to the database...", "green"))
        else:
            print(colored("No Products were added to the database...", "red"))

    def save_all(self):
        print(colored("Seeding Products...", "magenta"))
        self.save_brands()
        self.save_categories()
        self.save_subcategories()
        self.save_products()
