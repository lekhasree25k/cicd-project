# app.py - Simple Calculator Application
# CI/CD Mini Project - Python Application

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the division of two numbers. Raises error on divide by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def is_even(n):
    """Returns True if number is even, False otherwise."""
    return n % 2 == 0

def factorial(n):
    """Returns the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers!")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print("=== Calculator Application ===")
    print(f"add(10, 5)        = {add(10, 5)}")
    print(f"subtract(10, 5)   = {subtract(10, 5)}")
    print(f"multiply(10, 5)   = {multiply(10, 5)}")
    print(f"divide(10, 5)     = {divide(10, 5)}")
    print(f"is_even(4)        = {is_even(4)}")
    print(f"factorial(5)      = {factorial(5)}")
