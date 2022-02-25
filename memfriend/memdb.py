from collections import defaultdict
import sys
import typing

from memfriend import commands
from memfriend import constants


class DB:
    def __init__(self):
        self._store: typing.Dict = {}
        self._counts: defaultdict = defaultdict(int)
        self._transactions: typing.List[commands.Command] = []

    def dispatch(self, command: commands.Command):
        method = getattr(self, command.command_name())

        if method:
            return method(command)
        else:
            raise ValueError(f"Command {command} is invalid.")

    def end(self, _: commands.End) -> None:
        self._store.clear()
        self._counts.clear()
        sys.exit(0)

    def get(self, command: commands.Get) -> typing.Any:
        return self._store.get(command.name, constants.NULL_SENTINEL)

    def set(self, command: commands.Set) -> constants.Sentinel:
        self._store[command.name] = command.value
        self._counts[command.value] += 1
        return constants.SUCCESS_SENTINEL

    def unset(self, command: commands.Unset) -> constants.Sentinel:
        if command.name in self._store:
            value = self._store[command.name]
            self._counts[value] -= 1
            del self._store[command.name]

        return constants.SUCCESS_SENTINEL

    def numequalto(self, command: commands.Numequalto) -> int:
        return self._counts[command.value]
