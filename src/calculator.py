import math

def fun1(x, y):
    """
    Adds two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Sum of x and y.
        Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    
    return x + y

def fun2(x, y):
    """
    Subtracts two numbers.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Difference of x and y.
        Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x - y

def fun3(x, y):
    """
    Multiplies two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Product of x and y.
        Raises:
        ValueError: If either x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x * y

def fun4(x,y,z):
    """
    Adds three numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
        z (int/float): Third number.
    Returns:
        int/float: Sum of x, y and z.
    """
    total_sum = x + y + z
    return total_sum


# f1_op = fun1(2,3)
# f2_op = fun2(2,3)
# f3_op = fun3(2,3)
# f4_op = fun4(f1_op,f2_op,f3_op)


# Below are the features that I have added

# SQUARE ROOT

def square_root(x):
    """
    Calculates the square root of a number.
    Args:
        x (int/float): The number.
    Returns:
        float: Square root of x.
    Raises:
        ValueError: If x is not a number or is negative.
    """
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be a number.")
    if x < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(x)

# MEMORY BUTTONS

# Memory storage (starts empty, like a calculator's memory when switched on)
_memory = 0

def memory_add(value):
    """
    Adds a number to memory (M+).
    Args:
        value (int/float): Number to add to memory.
    Raises:
        ValueError: If value is not a number.
    """
    global _memory
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be a number.")
    _memory += value

def memory_subtract(value):
    """
    Subtracts a number from memory (M-).
    Args:
        value (int/float): Number to subtract from memory.
    Raises:
        ValueError: If value is not a number.
    """
    global _memory
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be a number.")
    _memory -= value

def memory_recall():
    """
    Returns the number currently stored in memory (MR).
    Returns:
        int/float: The stored value.
    """
    return _memory

def memory_clear():
    """
    Resets memory to zero (MC).
    """
    global _memory
    _memory = 0


# UNIT CONVERSIONS

KM_PER_MILE = 1.609344  # 1 mile is exactly 1.609344 km

def celsius_to_fahrenheit(c):
    """
    Converts a temperature from Celsius to Fahrenheit.
    Args:
        c (int/float): Temperature in Celsius.
    Returns:
        float: Temperature in Fahrenheit.
    Raises:
        ValueError: If c is not a number.
    """
    if not isinstance(c, (int, float)):
        raise ValueError("Input must be a number.")
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    """
    Converts a temperature from Fahrenheit to Celsius.
    Args:
        f (int/float): Temperature in Fahrenheit.
    Returns:
        float: Temperature in Celsius.
    Raises:
        ValueError: If f is not a number.
    """
    if not isinstance(f, (int, float)):
        raise ValueError("Input must be a number.")
    return (f - 32) * 5 / 9

def km_to_miles(km):
    """
    Converts a distance from kilometers to miles.
    Args:
        km (int/float): Distance in kilometers.
    Returns:
        float: Distance in miles.
    Raises:
        ValueError: If km is not a number or is negative.
    """
    if not isinstance(km, (int, float)):
        raise ValueError("Input must be a number.")
    if km < 0:
        raise ValueError("Distance cannot be negative.")
    return km / KM_PER_MILE

def miles_to_km(miles):
    """
    Converts a distance from miles to kilometers.
    Args:
        miles (int/float): Distance in miles.
    Returns:
        float: Distance in kilometers.
    Raises:
        ValueError: If miles is not a number or is negative.
    """
    if not isinstance(miles, (int, float)):
        raise ValueError("Input must be a number.")
    if miles < 0:
        raise ValueError("Distance cannot be negative.")
    return miles * KM_PER_MILE


# NUMBER BASE CONVERSIONS(decimal -> binary, decimal -> hex, and binary  decimal)

# Number base conversion
def decimal_to_binary(n):
    """
    Converts a whole number to binary.
    Args:
        n (int): A non-negative whole number.
    Returns:
        str: Binary form of n, e.g. 10 -> "1010".
    Raises:
        ValueError: If n is not a whole number or is negative.
    """
    if not isinstance(n, int):
        raise ValueError("Input must be a whole number.")
    if n < 0:
        raise ValueError("Input cannot be negative.")
    return bin(n)[2:]

def decimal_to_hex(n):
    """
    Converts a whole number to hexadecimal.
    Args:
        n (int): A non-negative whole number.
    Returns:
        str: Hexadecimal form of n, e.g. 255 -> "FF".
    Raises:
        ValueError: If n is not a whole number or is negative.
    """
    if not isinstance(n, int):
        raise ValueError("Input must be a whole number.")
    if n < 0:
        raise ValueError("Input cannot be negative.")
    return hex(n)[2:].upper()

def binary_to_decimal(b):
    """
    Converts a binary string back to a whole number.
    Args:
        b (str): A string of 0s and 1s, e.g. "1010".
    Returns:
        int: Decimal value, e.g. "1010" -> 10.
    Raises:
        ValueError: If b is not a string made only of 0s and 1s.
    """
    if not isinstance(b, str) or b == "" or any(ch not in "01" for ch in b):
        raise ValueError("Input must be a binary string of 0s and 1s.")
    return int(b, 2)