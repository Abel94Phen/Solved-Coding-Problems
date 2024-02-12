class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        
        target = self.head
        while index >= 0:
            target = target.next
            index -= 1
        return target.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        prev = self.head
        curr =self.head

        while curr:
            prev=curr
            curr = curr.next

        new_node = ListNode(val)
        prev.next = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        prev, curr = self.head, self.head
        while index >= 0:
            prev = curr
            curr = curr.next
            index -= 1
        new_node = ListNode(val) 
        prev.next = new_node       
        new_node.next = curr
        
        self.length += 1
        
        
        
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        prev, curr = self.head, self.head
        while index >= 0:
            prev = curr
            curr = curr.next
            index -= 1
        
        prev.next = curr.next
        self.length -= 1
        print(self.head)

## [] ==> [1] ==> [2] ==> [3]


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)