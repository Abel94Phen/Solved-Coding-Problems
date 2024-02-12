# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left, right = head, head
        while right:
            while right and right.val == left.val:
                right = right.next
            left.next = right
            left = right
        return head