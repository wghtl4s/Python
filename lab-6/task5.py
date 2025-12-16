import time

f = open("guest_book.txt", "a")
f.write("Created: " + time.ctime() + "\n")
f.close()

while True:
    name = input("Name (or 'exit'): ")
    if name == "exit":
        break
    
    greet = "Hello, " + name + "!"
    print(greet)
    
    now = time.ctime()
    f = open("guest_book.txt", "a")
    f.write(now + " - " + greet + "\n")
    f.close()

f = open("guest_book.txt", "a")
f.write("Last change: " + time.ctime() + "\n")
f.close()