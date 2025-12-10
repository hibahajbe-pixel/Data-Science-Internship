# Personal Finance Manager
## Overview
A command line personal finance manager to add, view and analyze expenses.

## How to run
1. Open terminal in project root.
2. Run `python -m src.main`

## Modules
- src/expense.py: Expense dataclass and validation
- src/file_manager.py: CSV read/write and backup
- src/main.py: Command line interface
- src/reports.py: Reporting helpers
- src/utils.py: small validators
- src/menu.py: small terminal helpers

## Data flow
User input -> Expense object -> in-memory list -> CSV persistence (data/expenses.csv)

## Submission contents
README.md, src/, data/, reports/, docs/, tests/, screenshots/, requirements.txt

## Future enhancements
- GUI or web front end
- Visual charts with matplotlib
- Export to Excel
- CI pipeline with unit tests
