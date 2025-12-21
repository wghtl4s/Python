class User:
    def __init__(self, first_name, last_name, nickname, email):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"Користувач: {self.first_name} {self.last_name}")

    def greeting_user(self):
        print(f"Вітаємо у системі, {self.nickname}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges:
    def __init__(self):
        self.privileges = ["Allowed to add message", "Allowed to delete users", "Allowed to ban users"]

    def show_privileges(self):
        print(f"Доступні привілеї: {', '.join(self.privileges)}")

class Admin(User):
    def __init__(self, first_name, last_name, nickname, email):
        super().__init__(first_name, last_name, nickname, email)
        self.priv = Privileges()

if __name__ == "__main__":
    user1 = User("Еліна", "Гришкова", "vtk251gea", "vtk251gea@test.com")
    user1.describe_user()
    user1.greeting_user()

    user1.increment_login_attempts()
    user1.increment_login_attempts()
    print(f"Кількість спроб входу: {user1.login_attempts}")
    user1.reset_login_attempts()
    print(f"Спроби після скидання: {user1.login_attempts}")

    admin_user = Admin("Ольга", "Ніщенка", "super_admin", "admin@system.ua")
    admin_user.priv.show_privileges()