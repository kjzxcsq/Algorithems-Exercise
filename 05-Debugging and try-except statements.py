def factorial(num):
    '''(int) -> (int)
    Calculates the factorial of a number, given by the variable num.
    '''
    # Check for errors in the input
    assert num >= 0, "num: Negative number is not allowed"

    # Initialize output to 1, not 0 (factorial of 0 is 1)
    output = 1

    # Use a while loop to calculate factorial
    while num > 0:
        output *= num  # Corrected *= operator
        num -= 1  # Corrected decrement operator

    return output

def calculate_years_to_double(principal, annual_interest_rate):
    '''(int , int) -> int
    Calculate the number of years required for the given principal to exceed double 
    with the provided annual interest rate using compound interest.
    '''
    # Assertion to check input validity
    assert principal >= 0, "Principal should be non-negative"
    assert 0 < annual_interest_rate <= 100, "Interest rate must be in the range (0, 100]"

    target_amount = principal * 2  # Fix: Should be double, not square
    amount = principal
    years = 0

    while amount < target_amount:  # Fix: Loop condition should be < instead of !=
        amount += amount * annual_interest_rate / 100  # Fix: Compound interest
        years += 1

    return years

def list_ratios(list_1, list_2):
    '''(list , list) -> list
    Returns a new list which has the elements list_1 / list_2.
    '''
    # Check if both lists have the same length
    assert len(list_1) == len(list_2), "Both lists must have the same length"

    new_list = []

    for i in range(len(list_1)):
        try:
            # Attempt to divide elements
            new_list.append(list_1[i] / list_2[i])
        except ZeroDivisionError:
            # Handle division by zero
            new_list.append('nan')
        except (TypeError, ValueError):
            # Handle type mismatch or invalid values
            new_list.append(None)

    return new_list
