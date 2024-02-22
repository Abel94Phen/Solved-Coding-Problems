# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        dummy = ListNode()
        dummy.next = head

        length = 0
        iterator = head
        while iterator:
            length += 1
            iterator = iterator.next

        partition_length = length // k
        extras = length % k

        answer = []
        for i in range(k):
            print(answer)
            iterator = dummy
            for _ in range(partition_length):
                iterator = iterator.next

            if extras:
                iterator = iterator.next
                extras -= 1

            
            temp = iterator.next
            iterator.next = None
            answer.append(dummy.next)
            dummy.next = temp


        return answer
                