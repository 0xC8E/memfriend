import collections
import sys
import typing

import iteration_utilities

from memfriend import commands
from memfriend import constants


class DB:
    def __init__(self):
        self._store: typing.Dict = {}
        self._counts: collections.defaultdict = collections.defaultdict(int)
        self._current_transaction: typing.List = None
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
        self._transactions.clear()
        self._current_transaction = None
        sys.exit(0)

    def get(self, command: commands.Get) -> typing.Any:
        if self._current_transaction is not None:
            self._current_transaction.append(command)
        else:
            return self._store.get(command.name, constants.NULL_SENTINEL)

    def set(self, command: commands.Set) -> constants.Sentinel:
        if self._current_transaction is not None:
            self._current_transaction.append(command)
        else:
            self._store[command.name] = command.value
            self._counts[command.value] += 1
            return constants.SUCCESS_SENTINEL

    def unset(self, command: commands.Unset) -> constants.Sentinel:
        if self._current_transaction is not None:
            self._current_transaction.append(command)
        else:
            if command.name in self._store:
                value = self._store[command.name]
                self._counts[value] -= 1
                del self._store[command.name]

            return constants.SUCCESS_SENTINEL

    def numequalto(self, command: commands.Numequalto) -> int:
        if self._current_transaction is not None:
            self._current_transaction.append(command)
        else:
            return self._counts[command.value]

    def begin(self, _: commands.Begin) -> None:
        if self._current_transaction is not None:
            self._transactions.append(self._current_transaction)
        self._current_transaction = []
        return constants.NO_RESULT_SENTINEL

    def rollback(self, _: commands.Rollback) -> constants.Sentinel:
        if self._current_transaction is None:
            return constants.NO_TRANSACTION_SENTINEL

        try:
            self._current_transaction = self._transactions.pop()
        except IndexError:
            self._current_transaction = None
        return constants.NO_RESULT_SENTINEL

    def commit(self, _: commands.Commit) -> constants.Sentinel:
        if self._current_transaction is None:
            return constants.NO_TRANSACTION_SENTINEL

        single_commands = iteration_utilities.deepflatten(
            self._transactions + self._current_transaction
        )
        self._current_transaction = None

        for command in single_commands:
            self.dispatch(command)
        return constants.NO_RESULT_SENTINEL
