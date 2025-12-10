from datetime import datetime

def validate_date(date_str):
    datetime.strptime(date_str, "%Y-%m-%d")
    return date_str

def validate_amount(amount):
    return float(amount)

def normalize_category(category):
    if not category:
        return "Other"
    return category.strip().title()
