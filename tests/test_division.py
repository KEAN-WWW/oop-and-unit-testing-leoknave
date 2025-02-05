"""
Unit tests for the divide function in the Calculator class.
"""

import pytest
from app.calculator import Calculator

def test_divide():
    """Tests the division method of Calculator."""
    calc = Calculator()
    assert calc.divide(10, 2) == 5
    assert calc.divide(-6, 3) == -2

def test_divide_zero_exception():
    """Tests that dividing by zero raises a ZeroDivisionError."""
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)

