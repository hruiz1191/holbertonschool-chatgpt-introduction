#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a given non-negative integer using recursion.

    Function Description:
    The factorial of a number `n` is the product of all positive integers 
    less than or equal to `n`. By definition, the factorial of 0 is 1. 
    This function uses recursion to compute the factorial, where the factorial
    of `n` is calculated as `n * factorial(n-1)`.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the input number `n`. For `n = 0`, the function returns 1.
    """
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:  # Recursive case: n * factorial(n-1)
        return n * factorial(n-1)

# Main program execution
if __name__ == "__main__":
    # Check if an argument is provided
    if len(sys.argv) < 2:
        print("Usage: ./factorial_recursive.py <number>")
    else:
        try:
            # Convert the first command-line argument to an integer
            num = int(sys.argv[1])
            if num < 0:
                print("Error: Factorial is not defined for negative numbers.")
            else:
                # Calculate and print the factorial
                f = factorial(num)
                print(f)
        except ValueError:
            print("Error: Please provide a valid integer.")

