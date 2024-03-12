# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #convert to array
        #remove subarrays that sum up to zero 
        #convert the array back to linked list
        numbers = []
        iterator = head
        while iterator:
            numbers.append(iterator.val)
            iterator = iterator.next

        hashmap = {}
        prefix_sum = 0
        for i in range(len(numbers)):
            prefix_sum += numbers[i]
            
            if prefix_sum == 0:
                x = 0
                while x <= i:
                    numbers[x] = None
                    x += 1
                hashmap = {}
            while prefix_sum in hashmap:
                x = hashmap[prefix_sum] + 1
                del hashmap[prefix_sum]
                prefix_sum += numbers[x]
                numbers[x] = None
                
            else:
                hashmap[prefix_sum] = i
                
        dummy = ListNode()
        iterator = dummy
        for num in numbers:
            if num:
                iterator.next = ListNode(num)
                iterator = iterator.next
        return dummy.next
