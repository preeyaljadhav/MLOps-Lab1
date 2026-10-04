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


# UNIT CONVERSION TEST CASES

def test_temperature_conversion():
    assert calculator.celsius_to_fahrenheit(100) == 212
    assert calculator.celsius_to_fahrenheit(0) == 32
    assert calculator.celsius_to_fahrenheit(-40) == -40
    assert calculator.fahrenheit_to_celsius(212) == 100
    assert calculator.fahrenheit_to_celsius(32) == 0
    assert calculator.fahrenheit_to_celsius(-40) == -40
    with pytest.raises(ValueError):
        calculator.celsius_to_fahrenheit("hot")

def test_distance_conversion():
    assert calculator.miles_to_km(1) == 1.609344
    assert calculator.km_to_miles(1.609344) == 1
    assert calculator.km_to_miles(0) == 0
    assert calculator.km_to_miles(10) == pytest.approx(6.2137, abs=0.0001)
    with pytest.raises(ValueError):
        calculator.km_to_miles(-5)
    with pytest.raises(ValueError):
        calculator.miles_to_km("far")


# NUMBER BASE CONVERSION TEST CASES

def test_base_conversion():
    assert calculator.decimal_to_binary(10) == "1010"
    assert calculator.decimal_to_binary(0) == "0"
    assert calculator.decimal_to_binary(255) == "11111111"
    assert calculator.decimal_to_hex(255) == "FF"
    assert calculator.decimal_to_hex(16) == "10"
    assert calculator.binary_to_decimal("1010") == 10
    assert calculator.binary_to_decimal("11111111") == 255
    assert calculator.binary_to_decimal(calculator.decimal_to_binary(42)) == 42
    with pytest.raises(ValueError):
        calculator.decimal_to_binary(-5)
    with pytest.raises(ValueError):
        calculator.decimal_to_binary(3.5)
    with pytest.raises(ValueError):
        calculator.decimal_to_hex("ten")
    with pytest.raises(ValueError):
        calculator.binary_to_decimal("102")