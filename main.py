import os
from collections import defaultdict

from src.expense import Expense
from src.file_manager import load_expenses, save_expenses, backup
from src.reports import category_summary, monthly_report
from src.menu import clear, pause

def safe_input(prompt):
    try:
        return input(prompt)
    except EOFError:
        return ""

def add_expense(expenses):
    try:
        amount = safe_input("Enter amount: ").strip()
        category = safe_input("Enter category (Food/Transport/Shopping/Other): ").strip().title() or "Other"
        date = safe_input("Enter date (YYYY-MM-DD): ").strip()
        desc = safe_input("Enter description: ").strip()

        e = Expense(amount=amount, category=category, date=date, description=desc)
        expenses.append(e)
        save_expenses(expenses)
        print("✅ Expense added successfully!")
    except Exception as exc:
        print("Error adding expense:", exc)
    pause()

def view_all(expenses):
    try:
        if not expenses:
            print("No expenses found.")
        else:
            for idx, e in enumerate(expenses, 1):
                print(f"{idx}. {e}")
    except Exception as exc:
        print("Error showing expenses:", exc)
    pause()

def show_category_summary(expenses):
    try:
        summary = category_summary(expenses)
        if not summary:
            print("No expenses yet.")
        else:
            for cat, total in summary.items():
                print(f"{cat}: ₹{total:.2f}")
    except Exception as exc:
        print("Error generating category summary:", exc)
    pause()

def generate_monthly(expenses):
    try:
        y_raw = safe_input("Enter year (YYYY): ").strip()
        m_raw = safe_input("Enter month (1-12): ").strip()
        y = int(y_raw)
        m = int(m_raw)
    except Exception:
        print("Invalid year or month input")
        pause()
        return

    try:
        report = monthly_report(expenses, y, m)
        print(f"Report for {y}-{m:02d}")
        print(f"Total: ₹{report['total']:.2f}")
        print(f"Average: ₹{report['average']:.2f}")
        print(f"Count: {report['count']}")
        print("Category breakdown:")
        for k, v in report['category_breakdown'].items():
            print(f'  {k}: ₹{v:.2f}')
    except Exception as exc:
        print("Error generating monthly report:", exc)
    pause()

def menu_loop():
    expenses = load_expenses()
    while True:
        clear()
        print("="*40)
        print("     PERSONAL FINANCE MANAGER")
        print("="*40)
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Category-wise Summary")
        print("4. Generate Monthly Report")
        print("5. Backup Data")
        print("6. Exit")
        choice = safe_input("Enter choice (1-6): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_all(expenses)
        elif choice == "3":
            show_category_summary(expenses)
        elif choice == "4":
            generate_monthly(expenses)
        elif choice == "5":
            try:
                dest = backup()
                print("Backup created at:", dest)
            except Exception as exc:
                print("Backup failed:", exc)
            pause()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")
            pause()

if __name__ == "__main__":
    print("Starting Personal Finance Manager... (press Ctrl+C to quit)")
    try:
        menu_loop()
    except KeyboardInterrupt:
        print("\nInterrupted by user, exiting.")
    except Exception as e:
        print("Unhandled error in main:", repr(e))
