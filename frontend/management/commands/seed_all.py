from django.core.management.base import BaseCommand

from accounts.seeders import Seed as SeedAcc
from products.seeders import Seed as SeedProd
from termcolor import colored


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'Seeding data to db'

    def handle(self, *args, **options):
        print(colored("Seeding data to the database...", "green"))
        sdac = SeedAcc()
        sdproduct = SeedProd()
        sdac.save_all()
        sdproduct.save_all()
