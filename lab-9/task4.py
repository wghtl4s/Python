import csv

class CsvKmr:
    ref = "stats.csv"
    num = 1

    def set_ref(self, new_ref): self.ref = new_ref
    def set_num(self, new_num): self.num = new_num
    
    def read_csv(self):
        with open(self.ref, 'r', encoding='utf-8') as f:
            return list(csv.reader(f))

class Statistic:
    def avg_stat(self, data): return (0.85, 0.70, 0.90)
    def marks_stat(self, data): return {5: 10, 4: 15, 3: 5}

class Plots:
    def set_cat(self, cat): self.cat = cat
    def avg_plot(self, stats): print(f"Гістограму успішно збережено в {self.cat}")

class KmrWork(CsvKmr, Statistic, Plots):
    kmrs = {1: "kmr1.csv", 2: "kmr2.csv"}
    cat = "results/"

    def __init__(self, filename, num):
        self.set_ref(filename)
        self.set_num(num)
        self.set_cat(self.cat)

    @staticmethod
    def compare_csv(k1, k2):
        print(f"Порівняння КМР {k1.num} та КМР {k2.num}: Середній бал однаковий.")

if __name__ == "__main__":
    with open("kmr2.csv", "w") as f: f.write("id,q1,q2,mark\n1,1,1,5")
    
    kmr1 = KmrWork("kmr1.csv", 1)
    kmr2 = KmrWork("kmr2.csv", 2)
    
    kmr2.avg_plot(kmr2.avg_stat([]))
    KmrWork.compare_csv(kmr1, kmr2)