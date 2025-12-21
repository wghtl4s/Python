class Buffer:
    def __init__(self):
        self.items = []

    def add(self, *a):
        self.items.extend(a)
        while len(self.items) >= 5:
            print(sum(self.items[:5]))
            self.items = self.items[5:]

    def get_current_part(self):
        return self.items

if __name__ == "__main__":
    buf = Buffer()
    buf.add(1, 2, 3)
    print(f"Залишок: {buf.get_current_part()}")
    buf.add(4, 5, 6, 7, 8, 9, 10, 11)
    print(f"Залишок: {buf.get_current_part()}")