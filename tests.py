__author__ = 'inwiter'

from loops import *


def test_name():
    name_str = name()
    assert name_str == "Python"


def test_get_name():
    str_name = get_name("Ravikant")
    assert str_name == "Ravikant"