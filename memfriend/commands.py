from dataclasses import dataclass
from typing import Any


@dataclass
class Command:
    pass


@dataclass
class End(Command):
    pass


@dataclass
class Get(Command):
    name: str


@dataclass
class Set(Command):
    name: str
    value: Any


@dataclass
class Unset(Command):
    name: str


@dataclass
class Numequalto(Command):
    value: Any
