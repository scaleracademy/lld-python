import unittest
from database import Database
from threading import Thread


class TestDatabaseMetaclass(unittest.TestCase):
    def test_singleton(self):
        db1 = Database()
        db2 = Database()

        self.assertEqual(
            id(db1),
            id(db2),
            "If the singleton pattern is implemented correctly, the two instances should be the same",
        )

    def test_thread_safety(self):
        threads = [Thread(target=lambda: Database()) for _ in range(10)]
        [t.start() for t in threads]
        instances = [t.join() for t in threads]

        self.assertTrue(all(id(i) == id(instances[0]) for i in instances))


if __name__ == "__main__":
    unittest.main()
