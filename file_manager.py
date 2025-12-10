import csv
import os
import shutil
from datetime import datetime
from typing import List
from src.expense import Expense

ROOT = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(ROOT, "data")
DEFAULT_FILE = os.path.join(DATA_DIR, "expenses.csv")
BACKUP_DIR = os.path.join(DATA_DIR, "backups")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(BACKUP_DIR, exist_ok=True)

def save_expenses(expenses: List[Expense], filename=DEFAULT_FILE):
    temp_file = filename + ".tmp"
    with open(temp_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Category", "Amount", "Description"])
        for e in expenses:
            writer.writerow(e.to_row())
    os.replace(temp_file, filename)

def load_expenses(filename=DEFAULT_FILE) -> List[Expense]:
    if not os.path.exists(filename):
        return []

    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        rows = list(reader)

    expenses = []
    for row in rows:
        try:
            expenses.append(Expense.from_row(row))
        except Exception:
            continue
    return expenses

def backup(filename=DEFAULT_FILE):
    if not os.path.exists(filename):
        raise FileNotFoundError("Data file not found for backup")
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(BACKUP_DIR, f"backup_{ts}.csv")
    shutil.copy2(filename, dest)
    return dest
