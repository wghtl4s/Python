f = open("numbers.txt", "r")
lines = f.readlines()
f.close()

total = 0
for line in lines:
    total = total + int(line.strip())

print(total)

f_sum = open("sum_numbers.txt", "w")
f_sum.write(str(total))
f_sum.close()