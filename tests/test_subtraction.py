"""
Unit tests for the subtract function in the Calculator class.
"""

import pytest
from app.calculator import Calculator

def test_subtract():
    """Tests the subtraction method of Calculator."""
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(0, 5) == -5
    assert calc.subtract(-2, -2) == 0

