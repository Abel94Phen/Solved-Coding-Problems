# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        length_A = 0
        dummy = headA
        while dummy:
            length_A += 1
            dummy = dummy.next

        length_B = 0
        dummy = headB
        while dummy:
            length_B += 1
            dummy = dummy.next

        correction = abs(length_A - length_B)
        if length_A - length_B == correction:
            while correction:
                headA = headA.next
                correction -= 1
        elif length_B - length_A == correction:
            while correction:
                headB = headB.next
                correction -= 1
            
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA