from memfriend import commands
from memfriend import constants


def test_rollback(db):
    name = "test"

    db.begin(commands.Begin())
    db.set(commands.Set(name=name, value=10))
    db.rollback(commands.Rollback())
    db.commit(commands.Commit())

    assert name not in db._store


def test_commit(db):
    name = "test"

    db.begin(commands.Begin())
    db.set(commands.Set(name=name, value=10))
    db.commit(commands.Commit())

    assert name in db._store
