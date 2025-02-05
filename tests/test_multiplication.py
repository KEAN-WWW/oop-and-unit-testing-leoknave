"""
Unit tests for the multiply function in the Calculator class.
"""

from app.calculator import Calculator  # Removed `pytest`

def test_multiply():
    """Tests the multiplication method of Calculator."""
    calc = Calculator()
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0, 5) == 0
