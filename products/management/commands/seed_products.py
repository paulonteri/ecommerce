from os import listdir, path
from termcolor import colored

from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand

from products.models import Brand, Category

base_dir = settings.BASE_DIR
images_dir = base_dir + "/media/images/static"
brands_dir = images_dir + "/brands"
categories_dir = images_dir + "/catalog"


class Seed:

    def save_brands(self):
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
            print(colored("Successfully added "+str(count) +
                          " Brands to the database...", "green"))
        else:
            print(colored("No Brands were added to the database...", "red"))

    def save_categories(self):
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
            print(colored("Successfully added "+str(count) +
                          " Categories to the database...", "green"))
        else:
            print(colored("No Categories were added to the database...", "red"))

    def save_all(self):
        self.save_brands()
        self.save_categories()


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'Seed products to db'

    def handle(self, *args, **options):
        print("Adding product information to the database...")
        sd = Seed()
        sd.save_all()
