# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        prev, curr = head, head.next
        while curr:
            if curr.val >= prev.val:
                prev = curr
                curr = curr.next
                continue
            iterator = dummy
            while curr.val > iterator.next.val:
                iterator = iterator.next

            prev.next = curr.next
            curr.next = iterator.next
            iterator.next = curr
            curr = prev.next
        return dummy.next
