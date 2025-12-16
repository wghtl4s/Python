from datetime import datetime

def is_valid_date(date_str):
    try:
        if not isinstance(date_str, str): return False
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except:
        return False

def analyze_expenses(expenses):
    cat_totals = {}
    max_exp = None
    invalid_dates = []
    errors = []
    
    for e in expenses:
        if not isinstance(e, tuple) or len(e) != 3:
            errors.append(e)
            continue
            
        amount, cat, date = e
        
        if not isinstance(amount, (int, float)) or not isinstance(cat, str) or cat is None:
            errors.append(e)
            continue
            
        if not is_valid_date(date):
            if date is not None:
                invalid_dates.append(date)
            errors.append(e)
            continue
            
        if cat in cat_totals:
            cat_totals[cat] += amount
        else:
            cat_totals[cat] = amount
            
        if max_exp is None or amount > max_exp[0]:
            max_exp = e
            
    return {
        "category_totals": cat_totals,
        "max_expense": max_exp,
        "invalid_dates": invalid_dates,
        "errors": errors
    }

data = [
    (100, "офіс", "2024-06-01"),
    (200, "маркетинг", "2024-06-02"),
    (50, "офіс", "2024-13-01"),
    (None, "маркетинг", "2024-06-02")
]

print(analyze_expenses(data))