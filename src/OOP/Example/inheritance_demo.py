# User
# Moderator


class User:
    def __init__(self, username, id_):
        self.username = username
        self.id_ = id_

    def send_message(self, message):
        print(f"{self.username}: {message}")

class Moderator(User):
    def __init__(self, username, _id, permission):
        super().__init__(username, _id) # super() metodunda self göndermemize gerek yok
        self.permission = permission

    def show_permission(self):
        print(f"{self.username} have a {self.permission} permission")

user = User("Abduley", 123141243)
user.send_message("Hello World!")

moderator = Moderator("Abduley", 123141243, "Ban Member")
moderator.show_permission()
