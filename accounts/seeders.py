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

    def save_all(self):
        self.add_admins()
