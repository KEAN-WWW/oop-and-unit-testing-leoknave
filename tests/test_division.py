import pytest
from app.calculator import Calculator  # Ensure this matches your actual file structure

def test_division():
    calc = Calculator()
    result = calc.divide(10, 2)  # Expected: 10 ÷ 2 = 5
    assert result == 5

def test_divide_zero_exception():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)  # Should raise ZeroDivisionError

