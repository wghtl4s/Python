import csv

f = open('marks.lab6.csv', 'r', encoding='utf-8')
reader = csv.reader(f)
data = list(reader)
f.close()

total_students = len(data)
print("Students count:", total_students)

marks_dist = {}
for row in data:
    mark = row[4].replace(',', '.')
    if mark in marks_dist:
        marks_dist[mark] = marks_dist[mark] + 1
    else:
        marks_dist[mark] = 1

for m in sorted(marks_dist.keys()):
    print("Mark:", m, "Students:", marks_dist[m])

time_sums = {}
time_counts = {}

for row in data:
    time_str = row[3]
    minutes = 0
    parts = time_str.split()
    if "хв" in parts:
        idx = parts.index("хв")
        minutes = int(parts[idx-1])
    
    mark = float(row[4].replace(',', '.'))
    
    if minutes in time_sums:
        time_sums[minutes] = time_sums[minutes] + mark
        time_counts[minutes] = time_counts[minutes] + 1
    else:
        time_sums[minutes] = mark
        time_counts[minutes] = 1

for m in sorted(time_sums.keys()):
    avg = time_sums[m] / time_counts[m]
    print(m, "min:", round(avg, 2))

f_res = open("marks_stats.txt", "w", encoding='utf-8')

for i in range(5, 25):
    correct = 0
    for row in data:
        score = float(row[i].replace(',', '.'))
        if score > 0:
            correct = correct + 1
    
    p_correct = (correct / total_students) * 100
    p_incorrect = 100 - p_correct
    f_res.write("Q" + str(i-4) + ": " + str(round(p_correct, 1)) + "% / " + str(round(p_incorrect, 1)) + "%\n")

ratios = []
for row in data:
    mark = float(row[4].replace(',', '.'))
    total_sec = 0
    parts = row[3].split()
    if "хв" in parts:
        total_sec = total_sec + int(parts[parts.index("хв")-1]) * 60
    if "сек" in parts:
        total_sec = total_sec + int(parts[parts.index("сек")-1])
    
    if total_sec > 0:
        ratio = mark / total_sec
        ratios.append((ratio, mark, row[3]))

ratios.sort(reverse=True)

f_res.write("\nTOP 5:\n")
for i in range(min(5, len(ratios))):
    res = ratios[i]
    f_res.write("Mark: " + str(res[1]) + " Time: " + str(res[2]) + "\n")

f_res.close()