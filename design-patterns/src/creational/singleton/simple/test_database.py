import unittest
from database import Database


class TestDatabaseSimple(unittest.TestCase):
    def test_private_constructor(self):
        with self.assertRaises(Exception) as context:
            Database()

        self.assertTrue(
            "Cannot instantiate Database class" in str(context.exception),
            "If the singleton pattern is implemented correctly, the constructor should be private",
        )
    
    def test_singleton(self):
        db1 = Database.get_instance()
        db2 = Database.get_instance()

        self.assertEqual(
            id(db1),
            id(db2),
            "If the singleton pattern is implemented correctly, the two instances should be the same",
        )

if __name__ == "__main__":
    unittest.main()
