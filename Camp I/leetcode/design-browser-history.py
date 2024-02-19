class BrowserHistory:

    def __init__(self, homepage: str):
        head = ListNode(homepage)
        self.dummy = ListNode
        self.dummy.next = head
        self.curr = head
        self.length = 1

    def visit(self, url: str) -> None:
        node = ListNode(url)
        iterator = self.dummy
        while iterator != self.curr:
            iterator = iterator.next
        iterator.next = node
        self.curr = self.curr.next
        self.length += 1


    def back(self, steps: int) -> str:
        if steps >= self.length - 1:
            self.curr = self.dummy.next
            self.length = 1
            return self.curr.val
        else:
            iterator = self.dummy.next
            i = 1
            while i < self.length - steps:
                iterator = iterator.next
                i += 1
            self.curr = iterator
            self.length -= steps
            return self.curr.val

    def forward(self, steps: int) -> str:
        iterator = self.curr
        i = 0
        while iterator and iterator.next and i < steps:
            iterator = iterator.next
            i += 1
        
        self.curr = iterator
        self.length += i
        
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)