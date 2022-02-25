import pytest

from memfriend import memdb


@pytest.fixture
def db():
    return memdb.DB()
