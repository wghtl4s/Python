def analyze_nested_categories(data):
    all_categories = []
    totals = {}
    
    stack = [data]
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            for item in current:
                stack.append(item)
        elif isinstance(current, dict):
            for cat, val in current.items():
                if cat not in all_categories:
                    all_categories.append(cat)
                if cat in totals:
                    totals[cat] += val
                else:
                    totals[cat] = val
                    
    return all_categories, totals

nested_data = [
    [{"офіс": 100}, {"маркетинг": 200}],
    [[{"офіс": 50}, {"маркетинг": 150}]],
    {"офіс": 200},
    {"офіс": 300},
    [{"офіс": 100, "extra": 1}]
]

res = analyze_nested_categories(nested_data)
print(res)