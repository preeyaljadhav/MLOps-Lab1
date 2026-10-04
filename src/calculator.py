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