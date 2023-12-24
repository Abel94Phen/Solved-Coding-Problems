class ATM:

    def __init__(self):
        self.denominations = [20, 50, 100, 200, 500]
        self.notes = [0, 0, 0, 0, 0]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.notes[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        withdraw_notes = [0]*5
        
        for i in range(len(self.notes) - 1, -1, -1):
            num_notes = min(amount // self.denominations[i], self.notes[i])
            withdraw_notes[i] = num_notes
            amount -= num_notes * self.denominations[i]

        if amount:
            return [-1]
        
        for i in range(len(self.notes)):
            self.notes[i] -= withdraw_notes[i]

        return withdraw_notes


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)