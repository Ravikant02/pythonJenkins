__author__ = 'inwiter'

from loops import name


def test_name():
    name_str = name()
    assert name_str == "Python"
