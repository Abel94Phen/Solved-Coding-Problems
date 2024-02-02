class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        C = len(set(nums))
        window = dict()
        subarrays = 0
        left = 0
        for right in range(len(nums)):
            window[nums[right]] = window.get(nums[right], 0) + 1

            while len(window) == C:
                subarrays += len(nums) - right
                
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1
        return subarrays
