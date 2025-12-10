from collections import defaultdict

def category_summary(expenses):
    summary = defaultdict(float)
    for e in expenses:
        summary[e.category] += e.amount
    return summary

def monthly_report(expenses, year, month):
    filtered = []
    for e in expenses:
        y, m, _ = e.date.split("-")
        if int(y) == year and int(m) == month:
            filtered.append(e)

    total = sum(e.amount for e in filtered)
    avg = total / len(filtered) if filtered else 0

    return {
        "total": total,
        "average": avg,
        "count": len(filtered),
        "category_breakdown": category_summary(filtered),
    }
