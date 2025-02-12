"""
Unit tests for the add function in the Calculator class.
"""

from app.calculator import Calculator  # Importing the Calculator class

def test_add():
    """Tests the addition method of Calculator."""
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0
    assert calc.add(100, 200) == 300
