def add(num1, num2):
    '''(int, int) -> int
    Adds two numbers and returns the result.
    '''
    return num1 + num2

def subtract(num1, num2):
    '''(int, int) -> int
    Subtracts num2 from num1 and returns the result.
    '''
    return num1 - num2

def multiply(num1, num2):
    '''(int, int) -> int
    Multiplies two natural numbers using addition and recursion.
    '''
    # Assertion to check inputs are integers
    assert isinstance(num1, int) and isinstance(num2, int), "Inputs must be integers"
    # Base condition: if either number is less than 1, return 0
    if num1 < 1 or num2 < 1:
        return 0
    # Recursive case: add num1 to the result of multiply(num1, num2 - 1)
    return add(num1, multiply(num1, subtract(num2, 1)))

def division(num1, num2):
    '''(int, int) -> int
    Divides num1 by num2 using subtraction, addition, and recursion.
    Returns the integer division result.
    '''
    # Assertion to check inputs are integers
    assert isinstance(num1, int) and isinstance(num2, int), "Inputs must be integers"
    # Base condition 1: if num1 < 1, return 0
    if num1 < 1:
        return 0
    # Base condition 2: handle zero division
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    # Recursive case: subtract num2 from num1 and increment the quotient
    if num1 < num2:
        return 0
    return add(1, division(subtract(num1, num2), num2))
