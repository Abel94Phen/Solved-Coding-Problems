# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        left, right = 0, len(nums) - 1
        while left < right and nums[left] == nums[right]:
            left += 1
            right -= 1
        
        if left >= right:
            return True
        return False