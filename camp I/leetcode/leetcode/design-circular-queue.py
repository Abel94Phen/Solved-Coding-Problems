class MyCircularQueue:

    def __init__(self, k: int):
        self.array = [-1 for _ in range(k + 1)]
        self.length = k + 1
        self.rear = 0
        self.front = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.rear = (self.rear + 1) % (self.length)
            self.array[self.rear] = value
            print(self.Rear())
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.front = (self.front + 1) % (self.length)
            return True


    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.array[(self.front + 1)%(self.length)]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.array[self.rear]

    def isEmpty(self) -> bool:
        if self.rear == self.front:
            return True
        return False

    def isFull(self) -> bool:
        if (self.rear + 1) % (self.length) == self.front:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()