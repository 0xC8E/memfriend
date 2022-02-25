from memfriend import commands
from memfriend import constants


def test_set(db):
    name = "test"
    value = 1
    set_command = commands.Set(name=name, value=value)

    assert name not in db._store

    db.set(set_command)
    assert db._store[name] == value


def test_get(db):
    name = "test"
    value = 1
    get_command = commands.Get(name=name)

    assert db.get(get_command) == constants.NULL_SENTINEL

    db._store[name] = value
    assert db.get(get_command) == value


def test_unset(db):
    name = "test"
    value = 1
    unset_command = commands.Unset(name=name)
    db._store[name] = value

    assert db.unset(unset_command) == constants.SUCCESS_SENTINEL
    assert name not in db._store


def test_numequalto(db):
    base_name = "test"
    max_count = 3
    value = 100
    numequalto_command = commands.Numequalto(value=value)

    assert db.numequalto(numequalto_command) == 0

    for i in range(1, max_count + 1):
        name = f"{base_name}{i}"
        set_command = commands.Set(name=name, value=value)
        db.set(set_command)

        assert db.numequalto(numequalto_command) == i

    unset_command = commands.Unset(name=name)
    db.unset(unset_command)

    assert db.numequalto(numequalto_command) == (max_count - 1)
