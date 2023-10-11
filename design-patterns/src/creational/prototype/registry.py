from abc import ABC, abstractmethod
from typing import Optional

from user import User


class UserRegistry(ABC):
    @abstractmethod
    def get_prototype(self, role: str) -> Optional[User]:
        pass

    @abstractmethod
    def add_prototype(self, role: str, user: User) -> None:
        pass

    def clone(self, role: str) -> Optional[User]:
        prototype = self.get_prototype(role)
        if prototype is None:
            raise Exception(f"Prototype with role {role} not found")

        return prototype.clone()
