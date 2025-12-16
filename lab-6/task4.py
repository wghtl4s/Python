import os

if not os.path.exists("new_dir"):
    os.mkdir("new_dir")

f_in = open("learning_python.txt", "r")
lines = f_in.readlines()
f_in.close()

f_current = open("new_dir/c_learning.txt", "w")
f_false = open("new_dir/false_statements.txt", "w")

for line in lines:
    new_line = line.replace("Python", "C")
    print("Phrase:", new_line.strip())
    choice = input("Is this true for C? (y/n): ")
    
    if choice == "y":
        f_current.write(new_line)
    else:
        f_false.write(new_line)

f_current.close()
f_false.close()