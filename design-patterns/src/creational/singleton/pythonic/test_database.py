import unittest
from database import Database


class TestDatabasePythonic(unittest.TestCase):
    def test_singleton(self):
        db1 = Database()
        db2 = Database()

        self.assertEqual(
            id(db1),
            id(db2),
            "If the singleton pattern is implemented correctly, the two instances should be the same",
        )

if __name__ == "__main__":
    unittest.main()
