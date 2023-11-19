from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    profile_image: str = None