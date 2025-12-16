import time

start_time = time.time()

f = open("text_3000.txt", "r")
text = f.read().lower()
f.close()

words = text.split()
counts = {}

for w in words:
    if w in counts:
        counts[w] = counts[w] + 1
    else:
        counts[w] = 1

print(counts)

end_time = time.time()
duration = end_time - start_time

f_res = open("analysis_results.txt", "w")
f_res.write("Created: " + time.ctime() + "\n")
f_res.write("Duration: " + str(duration) + " sec\n")
f_res.write(str(counts))
f_res.close()