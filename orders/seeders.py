import termcolor

from accounts.models import User
from orders.services.cart import add_to_cart
from products.models import Item


class Seed:
    added_users = 0
    added_items = 0

    users = User.objects.all()
    items = Item.objects.all()

    def seed_add_to_cart(self):
        try:
            for user in self.users:
                for item in self.items:
                    add_to_cart(user, item)
                    self.added_items += 1
                for item in self.items:
                    add_to_cart(user, item)
                    self.added_items += 1
                self.added_users += 1
        except Exception as e:
            print("Error: \n" + str(e))

        if self.added_items > 0 or self.added_users > 0:
            print(termcolor.colored("Successfully added " + str(self.added_items) +
                                    " Items to the carts of " + str(self.added_users) + " Users...", "green"))
        else:
            print(termcolor.colored("No Admins were added to the database...", "red"))

    def save_all(self):
        print(termcolor.colored("Seeding Add Items to Cart...", "magenta"))
        self.seed_add_to_cart()
