import fileinput

from memfriend import commands
from memfriend import constants
from memfriend import memdb


def start():
    db = memdb.DB()

    for line in fileinput.input():
        command = parse_command(line)
        result = db.dispatch(command)
        print(result)


def parse_command(command: str) -> commands.Command:
    parts = command.replace(constants.NEWLINE, "").split(constants.COMMAND_SEPARATOR)
    command_name = parts[0].lower()

    if command_name == commands.End.command_name():
        return commands.End()

    if command_name == commands.Get.command_name():
        name = parts[1]
        return commands.Get(name=name)

    if command_name == commands.Set.command_name():
        name = parts[1]
        value = parts[2]
        return commands.Set(name=name, value=value)

    if command_name == commands.Unset.command_name():
        name = parts[1]
        return commands.Unset(name=name)

    if command_name == commands.Numequalto.command_name():
        value = parts[1]
        return commands.Numequalto(value=value)


if __name__ == "__main__":
    start()
