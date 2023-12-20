class RandomizedSet:

    def __init__(self):
        self.indices = dict()
        self.numbers = []

    def insert(self, val: int) -> bool:
        if val in self.numbers:
            return False
        self.numbers.append(val)
        self.indices[val] = len(self.numbers) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numbers:
            return False
        
        i = self.indices[val]
        self.indices[self.numbers[-1]] = i
        self.numbers[i] = self.numbers[-1]
        self.indices.pop(val)
        self.numbers.pop()
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.numbers)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()