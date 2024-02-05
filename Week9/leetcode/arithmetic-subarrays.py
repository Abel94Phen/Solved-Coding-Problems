class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for i in range(len(l)):
            left, right = l[i], r[i]
            values = []
            while left <= right:
                values.append(nums[left])
                left += 1
            values.sort()
            diff = values[1] - values[0]
            for j in range(1, len(values) - 1):
                if values[j + 1] - values[j] != diff:
                    result.append(False)
                    break
            else:
                result.append(True)
                
        return result
