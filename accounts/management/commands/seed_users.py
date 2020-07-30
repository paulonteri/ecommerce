from django.core.management.base import BaseCommand

from accounts.seeders import Seed


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'Seed Users to db'

    def handle(self, *args, **options):
        print("Adding user information to the database...")
        sd = Seed()
        sd.save_all()
