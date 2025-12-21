import random

class Coin:
    def __init__(self):
        self._sideup = random.choice(['heads', 'tails'])

    def toss(self):
        self._sideup = random.choice(['heads', 'tails'])

    def get_sideup(self):
        return self._sideup

if __name__ == "__main__":
    my_coin = Coin()
    n = 5
    for i in range(n):
        my_coin.toss()
        print(f"Підкидання {i+1}: {my_coin.get_sideup()}")