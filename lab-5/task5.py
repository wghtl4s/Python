def filter_reports(reports, output_format, keyword):
    filtered_reports = []
    count = 0
    errors = []
    
    for item in reports:
        if type(item) != tuple:
            errors.append(item)
            continue
            
        if len(item) != 3:
            errors.append(item)
            continue
            
        name = item[0]
        author = item[1]
        rep_format = item[2]
        
        if type(name) != str or type(author) != str or type(rep_format) != str:
            errors.append(item)
            continue
            
        if name == "" or author == "" or rep_format == "":
            errors.append(item)
            continue
            
        if rep_format == output_format:
            if keyword in name or keyword in author:
                filtered_reports.append(item)
                count = count + 1
                
    return {
        "filtered_reports": filtered_reports,
        "count": count,
        "errors": errors
    }

reports_list = [
    ("Звіт1", "Іван Іванов", "pdf"),
    ("Звіт2", "Олена Петрівна", "docx"),
    ("", "Іван Іванов", "pdf"),
    ("Звіт3", "", "pdf"),
    ("Звіт4", "Петро Сидоров", ""),
    "не кортеж",
    123,
    None,
    ("Звіт5",),
    ("Звіт6", "Іван Іванов"),
    ("Звіт7", "Іван Іванов", 123)
]

result = filter_reports(reports_list, "pdf", "Іва")

print(result)