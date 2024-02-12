# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## None 1 2 3 4 5
        slow, fast = head, head
        while fast and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow