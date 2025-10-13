"""
Tests for FastMCP server template.

Run with: pytest tests/
"""

import pytest
from server import calculator, process_text, CalculatorInput, TextProcessingInput


class TestCalculator:
    """Test calculator tool."""

    def test_addition(self):
        """Test addition operation."""
        result = calculator(CalculatorInput(a=10, b=5, operation="add"))
        assert result == 15.0

    def test_subtraction(self):
        """Test subtraction operation."""
        result = calculator(CalculatorInput(a=10, b=5, operation="subtract"))
        assert result == 5.0

    def test_multiplication(self):
        """Test multiplication operation."""
        result = calculator(CalculatorInput(a=10, b=5, operation="multiply"))
        assert result == 50.0

    def test_division(self):
        """Test division operation."""
        result = calculator(CalculatorInput(a=10, b=5, operation="divide"))
        assert result == 2.0

    def test_division_by_zero(self):
        """Test division by zero raises error."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calculator(CalculatorInput(a=10, b=0, operation="divide"))

    def test_invalid_operation(self):
        """Test invalid operation raises validation error."""
        with pytest.raises(ValueError):
            CalculatorInput(a=10, b=5, operation="invalid")


class TestTextProcessing:
    """Test text processing tool."""

    def test_uppercase(self):
        """Test uppercase operation."""
        result = process_text(
            TextProcessingInput(text="hello world", operation="uppercase")
        )
        assert result == "HELLO WORLD"

    def test_lowercase(self):
        """Test lowercase operation."""
        result = process_text(
            TextProcessingInput(text="HELLO WORLD", operation="lowercase")
        )
        assert result == "hello world"

    def test_reverse(self):
        """Test reverse operation."""
        result = process_text(
            TextProcessingInput(text="hello", operation="reverse")
        )
        assert result == "olleh"

    def test_word_count(self):
        """Test word count operation."""
        result = process_text(
            TextProcessingInput(text="hello world foo bar", operation="word_count")
        )
        assert result == "4"

    def test_invalid_operation(self):
        """Test invalid operation raises validation error."""
        with pytest.raises(ValueError):
            TextProcessingInput(text="test", operation="invalid")
