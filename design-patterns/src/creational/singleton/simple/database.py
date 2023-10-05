class Database:
    _instance = None

    def __init__(self):
        raise RuntimeError("Cannot instantiate Database class")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance
