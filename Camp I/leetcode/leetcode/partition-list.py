# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_head, right_head = ListNode(), ListNode()
        left, right = left_head, right_head
        iterator = head

        while iterator:
            if iterator.val < x:
                left.next = ListNode(iterator.val)
                left = left.next

            else:
                right.next = ListNode(iterator.val)
                right = right.next

            iterator = iterator.next

        left.next = right_head.next

        return left_head.next