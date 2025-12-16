f = open("learning_python.txt", "r")
lines = f.readlines()
f.close()

for line in lines:
    print(line.strip())

sorted_lines = sorted(lines, key=len, reverse=True)

print("--- Sorted ---")
for line in sorted_lines:
    print(line.strip())