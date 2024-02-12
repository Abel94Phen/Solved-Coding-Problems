# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        iterator = head
        while iterator:
            new_node = ListNode(iterator.val)
            new_node.next = dummy.next
            dummy.next = new_node
            iterator = iterator.next
        return dummy.next