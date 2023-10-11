from typing import Optional
from user import User
from registry import UserRegistry


class UserRegistryImpl(UserRegistry):
    def __init__(self):
        self.prototypes: dict[str, User] = {}

    def get_prototype(self, role: str) -> Optional[User]:
        if role not in self.prototypes:
            return None

        return self.prototypes[role]

    def add_prototype(self, role: str, user: User) -> None:
        self.prototypes[role] = user
