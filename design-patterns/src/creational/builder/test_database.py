import unittest
from database import Database


class TestDatabaseBuilder(unittest.TestCase):
    def test_builder_method(self):
        builder = Database.builder()
        self.assertTrue(
            type(builder) == Database.Builder,
            "If the builder method is called, it should return a builder object",
        )

    def test_build_method(self):
        print(Database.builder().host("localhost"))
        db = (
            Database.builder()
            .host("localhost")
            .port(3306)
            .username("root")
            .password("root")
            .build()
        )

        self.assertTrue(
            type(db) == Database,
            "If the build method is called, it should return a database object",
        )

        self.assertEqual(
            db.host,
            "localhost",
            "If the build method is called, it should return a database object with the correct host",
        )

        self.assertEqual(
            db.port,
            3306,
            "If the build method is called, it should return a database object with the correct port",
        )


if __name__ == "__main__":
    unittest.main()
