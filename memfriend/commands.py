from dataclasses import dataclass
from typing import Any


@dataclass
class Command:
    @classmethod
    def command_name(cls) -> str:
        return cls.__name__.lower()

    def __repr__(self) -> str:
        return f"{self.command_name}"


@dataclass
class End(Command):
    pass


@dataclass
class Get(Command):
    name: str

    def __repr__(self) -> str:
        return f"{super().__repr__()} {self.name}"


@dataclass
class Set(Command):
    name: str
    value: Any

    def __repr__(self) -> str:
        return f"{super().__repr__()} {self.name} {self.value}"


@dataclass
class Unset(Command):
    name: str

    def __repr__(self) -> str:
        return f"{super().__repr__()} {self.name}"


@dataclass
class Numequalto(Command):
    value: Any

    def __repr__(self) -> str:
        return f"{super().__repr__()} {self.value}"


@dataclass
class Begin(Command):
    pass


@dataclass
class Rollback(Command):
    pass


@dataclass
class Commit(Command):
    pass
