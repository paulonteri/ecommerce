from django.core.management.base import BaseCommand

from products.seeders import Seed


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'Seed products to db'

    def handle(self, *args, **options):
        print("Adding product information to the database...")
        sd = Seed()
        sd.save_all()
