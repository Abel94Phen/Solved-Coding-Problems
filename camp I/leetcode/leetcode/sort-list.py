# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        iterator = head
        while iterator:
            nums.append(iterator.val)
            iterator = iterator.next
        nums.sort()
        dummy = ListNode()
        iterator = dummy
        for i in range(len(nums)):
            iterator.next = ListNode(nums[i])
            iterator = iterator.next
        
        return dummy.next