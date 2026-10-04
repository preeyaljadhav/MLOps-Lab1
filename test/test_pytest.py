import pytest
from src import calculator

def test_fun1():
    assert calculator.fun1(2, 3) == 5
    assert calculator.fun1(5,0) == 5
    assert calculator.fun1 (-1, 1) == 0
    assert calculator.fun1 (-1, -1) == -2


def test_fun2():
    assert calculator.fun2(2, 3) == -1
    assert calculator.fun2(5,0) == 5
    assert calculator.fun2 (-1, 1) == -2
    assert calculator.fun2 (-1, -1) == 0

def test_fun3():
    assert calculator.fun3(2, 3) == 6
    assert calculator.fun3(5,0) == 0
    assert calculator.fun3 (-1, 1) == -1
    
    assert calculator.fun3 (-1, -1) == 1

def test_fun4():
    assert calculator.fun4(2, 3, 5) == 10
    assert calculator.fun4(5,0, -1) == 4
    assert calculator.fun4 (-1, -1, -1) == -3
    
    assert calculator.fun4 (-1, -1, 100) == 98

# My test cases for the functions I have added 

# SQARE ROOT TEST CASES

def test_square_root():
    assert calculator.square_root(16) == 4
    assert calculator.square_root(0) == 0
    assert calculator.square_root(2.25) == 1.5
    with pytest.raises(ValueError):
        calculator.square_root(-4)
    with pytest.raises(ValueError):
        calculator.square_root("nine")

# MEMORY BUTTONS TEST CASES

def test_memory():
    calculator.memory_clear()
    assert calculator.memory_recall() == 0
    calculator.memory_add(10)
    assert calculator.memory_recall() == 10
    calculator.memory_add(5)
    assert calculator.memory_recall() == 15
    calculator.memory_subtract(3)
    assert calculator.memory_recall() == 12
    calculator.memory_clear()
    assert calculator.memory_recall() == 0
    calculator.memory_add(calculator.fun1(2, 3))
    assert calculator.memory_recall() == 5
    calculator.memory_clear()
    with pytest.raises(ValueError):
        calculator.memory_add("ten")
    with pytest.raises(ValueError):
        calculator.memory_subtract("ten")