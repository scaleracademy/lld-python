import unittest
from user import User
from user_registry import UserRegistryImpl


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(1, "John", "Doe", "johndoe@example.com", "1234567890")
        self.registry = UserRegistryImpl()

    def test_clone(self):
        cloned_user = self.user.clone()

        self.assertIsNot(
            self.user,
            cloned_user,
            "If the clone method is implemented correctly, the cloned object should not be the same as the original object",
        )
        self.assertEqual(
            self.user.id,
            cloned_user.id,
            "If the clone method is implemented correctly, the cloned object should have the same attributes as the original object",
        )
        self.assertEqual(
            self.user.first_name,
            cloned_user.first_name,
            "If the clone method is implemented correctly, the cloned object should have the same attributes as the original object",
        )
        self.assertEqual(
            self.user.last_name,
            cloned_user.last_name,
            "If the clone method is implemented correctly, the cloned object should have the same attributes as the original object",
        )
        self.assertEqual(
            self.user.email,
            cloned_user.email,
            "If the clone method is implemented correctly, the cloned object should have the same attributes as the original object",
        )
        self.assertEqual(
            self.user.phone,
            cloned_user.phone,
            "If the clone method is implemented correctly, the cloned object should have the same attributes as the original object",
        )

    def test_add_to_registry(self):
        self.registry.add_prototype("Student", self.user)
        self.assertIn(
            "Student",
            self.registry.prototypes,
            "If the add_prototype method is implemented correctly, the prototype should be added to the registry",
        )

    def test_get_from_registry(self):
        self.registry.add_prototype("Teacher", self.user)
        user_from_registry = self.registry.get_prototype("Teacher")

        self.assertEqual(self.user.id, user_from_registry.id, "If the get_prototype method is implemented correctly, the prototype should be retrieved from the registry")
        self.assertEqual(self.user.first_name, user_from_registry.first_name, "If the get_prototype method is implemented correctly, the prototype should be retrieved from the registry")
        self.assertEqual(self.user.last_name, user_from_registry.last_name, "If the get_prototype method is implemented correctly, the prototype should be retrieved from the registry")
        self.assertEqual(self.user.email, user_from_registry.email, "If the get_prototype method is implemented correctly, the prototype should be retrieved from the registry")
        self.assertEqual(self.user.phone, user_from_registry.phone, "If the get_prototype method is implemented correctly, the prototype should be retrieved from the registry")


if __name__ == "__main__":
    unittest.main()
