import pytest
from src.expense import Expense

def test_expense_creation():
    e = Expense(amount=100, category="food", date="2024-01-01", description="test")
    assert e.amount == 100.0
    assert e.category == "Food"
    assert e.date == "2024-01-01"
    assert e.description == "test"
