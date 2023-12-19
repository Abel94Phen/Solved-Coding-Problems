class Bitset:
    def __init__(self, size):
        self.bits = [0 for _ in range(size)]
        self.bits_reversed = [1 for _ in range(size)]
        self.ones = 0
        self.zeros = size
        self.size = size

    def fix(self, idx):
        if not self.bits[idx]:
            self.ones += 1
            self.zeros -= 1
        self.bits[idx] = 1
        self.bits_reversed[idx] = 0

    def unfix(self, idx):
        if self.bits[idx]:
            self.ones -= 1
            self.zeros += 1
        self.bits[idx] = 0
        self.bits_reversed[idx] = 1

    def flip(self):
        self.bits, self.bits_reversed = self.bits_reversed, self.bits
        self.ones, self.zeros = self.zeros, self.ones

    def all(self):
        return self.ones == self.size

    def one(self):
        return self.ones > 0

    def count(self):
        return self.ones

    def toString(self):
        return ''.join(map(str, self.bits))


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()