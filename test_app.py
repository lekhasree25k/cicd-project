# test_app.py - Unit Tests for Calculator Application
# These tests are automatically run by the CI/CD pipeline on every commit

import pytest
from app import add, subtract, multiply, divide, is_even, factorial


# ── Tests for add() ──────────────────────────────────────────────────────────

def test_add_positive_numbers():
    assert add(3, 5) == 8

def test_add_negative_numbers():
    assert add(-3, -5) == -8

def test_add_zero():
    assert add(0, 5) == 5

def test_add_floats():
    assert add(1.5, 2.5) == 4.0


# ── Tests for subtract() ─────────────────────────────────────────────────────

def test_subtract_positive_numbers():
    assert subtract(10, 5) == 5

def test_subtract_gives_negative():
    assert subtract(3, 10) == -7

def test_subtract_zero():
    assert subtract(5, 0) == 5


# ── Tests for multiply() ─────────────────────────────────────────────────────

def test_multiply_positive_numbers():
    assert multiply(4, 5) == 20

def test_multiply_by_zero():
    assert multiply(4, 0) == 0

def test_multiply_negative_numbers():
    assert multiply(-3, -4) == 12

def test_multiply_mixed_sign():
    assert multiply(-3, 4) == -12


# ── Tests for divide() ───────────────────────────────────────────────────────

def test_divide_positive_numbers():
    assert divide(10, 2) == 5.0

def test_divide_returns_float():
    assert divide(7, 2) == 3.5

def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert "Cannot divide by zero" in str(exc_info.value)


# ── Tests for is_even() ──────────────────────────────────────────────────────

def test_is_even_returns_true_for_even():
    assert is_even(4) == True

def test_is_even_returns_false_for_odd():
    assert is_even(7) == False

def test_is_even_zero():
    assert is_even(0) == True

def test_is_even_negative_even():
    assert is_even(-2) == True


# ── Tests for factorial() ────────────────────────────────────────────────────

def test_factorial_of_zero():
    assert factorial(0) == 1

def test_factorial_of_one():
    assert factorial(1) == 1

def test_factorial_of_five():
    assert factorial(5) == 120

def test_factorial_of_ten():
    assert factorial(10) == 3628800

def test_factorial_negative_raises_error():
    with pytest.raises(ValueError) as exc_info:
        factorial(-1)
    assert "not defined for negative" in str(exc_info.value)
