from calculator import *
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_substract():
    assert subtract(10, 3) == 7

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(20, 4) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(20, 0)