from dataclasses import dataclass
from datetime import datetime

@dataclass
class Expense:
    amount: float
    category: str
    date: str  # YYYY-MM-DD
    description: str

    def __post_init__(self):
        # validate amount
        try:
            self.amount = float(self.amount)
        except Exception:
            raise ValueError("Amount must be a valid number")

        # validate date format
        try:
            datetime.strptime(self.date, "%Y-%m-%d")
        except Exception:
            raise ValueError("Date must be in YYYY-MM-DD format")

        # clean formatting
        self.category = self.category.strip().title()
        self.description = self.description.strip()

    def to_row(self):
        return [self.date, self.category, f"{self.amount:.2f}", self.description]

    @classmethod
    def from_row(cls, row):
        date, category, amount, description = row
        return cls(amount=float(amount), category=category, date=date, description=description)

    def __str__(self):
        return f"{self.date} | {self.category}: ₹{self.amount:.2f} - {self.description}"
