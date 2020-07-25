from os import listdir, path

from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand

from products.models import Brand, Category

base_dir = settings.BASE_DIR
images_dir = base_dir + "/media/images/static"
brands_dir = images_dir + "/brands"
categories_dir = images_dir + "/catalog"


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'Seed products to db'

    def save_brands(self):
        files = listdir(brands_dir)

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

    def save_categories(self):
        files = listdir(categories_dir)

        for i in files:
            file_path = categories_dir + "/" + i

            try:
                file_name = path.splitext(i)[0]

                with open(file_path, "rb") as f:
                    data = File(f)
                    obj = Category(title=file_name.capitalize())
                    obj.image.save(i, data, save=True)

            except Exception as e:
                print("Error: \n" + str(e))

    def handle(self, *args, **options):
        self.save_brands()
        self.save_categories()
