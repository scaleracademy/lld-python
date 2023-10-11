from __future__ import annotations
import copy
from time import sleep

from cloneable import Cloneable


class User(Cloneable):
    def __init__(
        self, id: int, first_name: str, last_name: str, email: str, phone: str
    ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

        sleep(5)  # Simulate API call

    def clone(self) -> User:
        return copy.deepcopy(self)
