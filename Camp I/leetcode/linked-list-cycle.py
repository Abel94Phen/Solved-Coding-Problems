# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Floyd's Tortoise and Hare Algorithm
        
        Tortoise = head
        Hare = head
        
        while Hare != None and Hare.next != None:
            Tortoise = Tortoise.next
            Hare = Hare.next.next
            if Tortoise == Hare:
                return True
            
        return False