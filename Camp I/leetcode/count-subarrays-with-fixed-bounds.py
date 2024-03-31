class Solution:
    def countSubarrays(self, nums: List[int], mink: int, maxK: int) -> int:
        subarrays = 0
        left_far = left_near = right_idx = -1

        for i, num in enumerate(nums) :
            if not mink <= num <= maxK:
                left_far = i

            if num == mink:
                left_near = i

            if num == maxK:
                right_idx = i

            subarrays += max(0, min(left_near, right_idx) - left_far)

        return subarrays
