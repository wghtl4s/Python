import unittest

class User:
    def __init__(self, first_name, last_name, nickname):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges:
    def __init__(self):
        self.privileges = ["Allowed to add message"]

class Admin(User):
    def __init__(self, first_name, last_name, nickname):
        super().__init__(first_name, last_name, nickname)
        self.priv = Privileges()

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("Еліна", "Тестовий", "elina_test")

    def test_full_name(self):
        self.assertEqual(self.user.first_name, "Еліна")
        self.assertEqual(self.user.last_name, "Тестовий")

    def test_login_attempts(self):
        self.user.increment_login_attempts()
        self.user.increment_login_attempts()
        self.assertEqual(self.user.login_attempts, 2)
        self.user.reset_login_attempts()
        self.assertEqual(self.user.login_attempts, 0)

    def test_admin_privileges(self):
        admin = Admin("Ольга Ніщенко", "Адмін", "boss")
        self.assertIn("Allowed to add message", admin.priv.privileges)

if __name__ == "__main__":
    unittest.main()