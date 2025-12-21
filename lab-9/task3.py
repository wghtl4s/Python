class Apple:
    states = {0: "Відсутнє", 1: "Цвітіння", 2: "Зелене", 3: "Червоне"}

    def __init__(self, index):
        self._index = index
        self._state = self.states[0]

    def grow(self):
        current_key = [k for k, v in self.states.items() if v == self._state][0]
        if current_key < 3:
            self._state = self.states[current_key + 1]

    def is_ripe(self):
        return self._state == self.states[3]

class AppleTree:
    def __init__(self, count):
        self.apples = [Apple(i) for i in range(count)]

    def grow_all(self):
        for apple in self.apples:
            apple.grow()

    def all_are_ripe(self):
        return all(apple.is_ripe() for apple in self.apples)

    def give_away_all(self):
        self.apples = []

class Gardener:
    def __init__(self, name, tree):
        self.name = name
        self._tree = tree

    def work(self):
        print(f"Садівник {self.name} працює...")
        self._tree.grow_all()

    def harvest(self):
        if self._tree.all_are_ripe():
            print("Урожай зібрано!")
            self._tree.give_away_all()
        else:
            print("Попередження: Яблука ще не дозріли!")

    @staticmethod
    def apple_base():
        print("Довідка: Стадії дозрівання - Відсутнє -> Цвітіння -> Зелене -> Червоне (стигле)")

if __name__ == "__main__":
    Gardener.apple_base()
    tree = AppleTree(5)
    worker = Gardener("Людмила", tree)
    worker.harvest()
    while not tree.all_are_ripe():
        worker.work()
    worker.harvest()