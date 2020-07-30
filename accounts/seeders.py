from termcolor import colored

from accounts.models import User


class Seed:
    admins = 0

    def add_admins(self):
        try:
            User.objects.create_superuser(1, "1@example.com", 1)
        except Exception as e:
            print("Error: \n" + str(e))
        else:
            self.admins += 1

        if self.admins > 0:
            print(colored("Successfully added " + str(self.admins) +
                          " Admins to the database...", "green"))
        else:
            print(colored("No Admins were added to the database...", "red"))

    def save_all(self):
        print(colored("Seeding Users...", "magenta"))
        self.add_admins()
