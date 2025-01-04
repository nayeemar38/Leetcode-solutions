class RandomizedSet:

    def __init__(self):
        self.random = set()

    def insert(self, val: int) -> bool:
        if val not in self.random:
            self.random.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.random:
            self.random.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.random))