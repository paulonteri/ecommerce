from django.core.management.base import BaseCommand

from accounts.seeders import Seed as SeedAccounts
from products.seeders import Seed as SeedProducts
from termcolor import colored


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'Seed data to db'

    def handle(self, *args, **options):
        print(colored("Seeding data to the database...", "blue"))
        try:
            sdusers = SeedAccounts()
            sdusers.save_all()
        except Exception as e:
            print("Error: \n" + str(e))
        try:
            sdproducts = SeedProducts()
            sdproducts.save_all()
        except Exception as e:
            print("Error: \n" + str(e))
        print(colored("Finished Seeding.", "blue"))
