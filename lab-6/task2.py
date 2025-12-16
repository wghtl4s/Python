import sys

args = sys.argv[1:]
f = open("parity_results.txt", "w")

for num in args:
    n = int(num)
    if n % 2 == 0:
        res = "парне"
    else:
        res = "непарне"
    f.write(num + " - " + res + "\n")

f.close()