# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        r = head
        while right > 1:
            r = r.next
            right -= 1
        right_side = r.next
        
        l = dummy
        left_side = dummy
        while left > 0:
            left_side = l
            l = l.next
            left -= 1

        prev, curr = None, l
        while prev != r:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        left_side.next = prev
        l.next = right_side

        return dummy.next