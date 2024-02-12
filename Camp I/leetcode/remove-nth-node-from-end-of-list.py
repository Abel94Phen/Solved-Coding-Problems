# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        length = 0
        while dummy != None:
            length += 1
            dummy = dummy.next
        
        if length == 1:
            return None
        
        if n == length:
            head = head.next
            return head
        prev, curr = head, head
        l = 0
        while l < length - n:
            prev = curr
            curr = curr.next
            l += 1
        prev.next = curr.next
        return head