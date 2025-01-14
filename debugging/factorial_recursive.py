import sys  # Importing sys to handle command-line arguments

def factorial(n):
    """
    Calculates the factorial of a given non-negative integer using recursion.

    Function Description:
    This function computes the factorial of a non-negative integer `n`. 
    The factorial of a number is defined as the product of all positive integers 
    less than or equal to that number. By definition, the factorial of 0 is 1.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the input number `n`.
    """
    if n == 0:  # Base case: the factorial of 0 is 1
        return 1
    else:  # Recursive case: n * factorial of (n-1)
        return n * factorial(n-1)

# Main program execution
# Reads an integer from command-line arguments, calculates its factorial, and prints the result
f = factorial(int(sys.argv[1]))  # Convert the first argument to an integer and calculate factorial
print(f)  # Print the result of the factorial
