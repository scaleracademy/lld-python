from threading import Lock


class SingletonMeta(type):
    _instances = {}

    def __call__(cls):
        if cls not in cls._instances:
            with Lock():
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__()
        return cls._instances[cls]
