# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = head
        
        if head == None or head.next == None:
            return head
        else:
            even = head.next
            new_head = even

        while even and even.next and odd and odd.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
            
        # [head] ==> [1]
        
        odd.next = new_head
        return head