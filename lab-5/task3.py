def analyze_clients(clients):
    status_count = {}
    invalid_emails = []
    new_clients = []
    errors = []
    
    for c in clients:
        if not isinstance(c, tuple) or len(c) != 3:
            errors.append(c)
            continue
            
        name, status, email = c
        
        if not isinstance(name, str) or not isinstance(status, str) or not isinstance(email, str):
            errors.append(c)
            continue
            
        if name == "" or status == "" or email == "":
            errors.append(c)
            continue
            
        if "@" not in email or "." not in email:
            invalid_emails.append(email)
            
        if status in status_count:
            status_count[status] += 1
        else:
            status_count[status] = 1
            
        if status == "новий":
            new_clients.append(name)
            
    return {
        "status_count": status_count,
        "invalid_emails": invalid_emails,
        "new_clients": new_clients,
        "errors": errors
    }

data = [
    ("Іван", "новий", "ivan@email.com"),
    ("Олена", "постійний", "olena[at]mail.com"),
    ("", "новий", "ivan@email.com"),
    ("Петро", "", ""),
    "не кортеж",
    (123, "новий", "ivan@email.com")
]

print(analyze_clients(data))