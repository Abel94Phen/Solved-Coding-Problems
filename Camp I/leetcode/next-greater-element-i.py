class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        for num in nums1:
            index = nums2.index(num)
            for i in range(index + 1, len(nums2)):
                if nums2[i] > num:
                    answer.append(nums2[i])
                    break
            else:
                answer.append(-1)
        return answer
            
