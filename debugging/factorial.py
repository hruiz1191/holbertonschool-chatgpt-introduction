#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a given non-negative integer.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the input number `n`.
    """
    result = 1
    while n > 1:
        result *= n  # Multiply result by n
        n -= 1       # Decrement n by 1
    return result

# Main program execution
if len(sys.argv) < 2:
    print("Usage: ./factorial.py <number>")
else:
    try:
        # Convert input argument to an integer
        num = int(sys.argv[1])
        if num < 0:
            print("Error: Factorial is not defined for negative numbers.")
        else:
            f = factorial(num)
            print(f)
    except ValueError:
        print("Error: Please provide a valid integer.")
