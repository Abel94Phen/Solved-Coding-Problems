# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        iterator = head
        length = 0
        while iterator != None:
            length += 1
            iterator = iterator.next
        mid = length//2
        iterator = head
        for _ in range(mid):
            iterator = iterator.next
        return iterator