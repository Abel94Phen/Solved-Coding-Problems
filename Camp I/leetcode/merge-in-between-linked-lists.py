# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(0,list1)
        left, right, end = dummy, dummy, list2
        diff = b - a + 1
    
        while end.next:
            end = end.next
        
        while diff:
            right = right.next
            diff -= 1

        while a:
            left = left.next
            right = right.next
            a -= 1

        left.next = list2
        end.next = right.next
        
        return dummy.next
