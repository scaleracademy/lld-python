from __future__ import (
    annotations,
)  # For type hinting the return type of the builder methods
from dataclasses import dataclass


@dataclass
class Database:
    host: str
    port: int
    username: str
    password: str

    @staticmethod
    def builder():
        return Database.Builder()

    class Builder:
        def __init__(self):
            self._host = None
            self._port = None
            self._username = None
            self._password = None

        def host(self, host: str) -> Database.Builder:
            self._host = host
            return self

        def port(self, port: int) -> Database.Builder:
            self._port = port
            return self

        def username(self, username: str) -> Database.Builder:
            self._username = username
            return self

        def password(self, password: str) -> Database.Builder:
            self._password = password
            return self

        def build(self) -> Database:
            self.validate()

            return Database(
                host=self._host,
                port=self._port,
                username=self._username,
                password=self._password,
            )

        def validate(self) -> None:
            if not self.is_host_reachable(self._host):
                raise Exception("Host is not reachable")
        
        def is_host_reachable(self, host) -> bool:
            # This method should check if the host is reachable
            # For the sake of simplicity, we will just return True
            return True
