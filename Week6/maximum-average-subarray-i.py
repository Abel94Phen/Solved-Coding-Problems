class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i,j = 0, k
        s = sum(nums[i:j])
        max_ave = s / k
        while j < len(nums):
            s -= nums[i]
            i += 1
             
            s += nums[j]
            j += 1
            max_ave = max(max_ave, s/k)
        return max_ave