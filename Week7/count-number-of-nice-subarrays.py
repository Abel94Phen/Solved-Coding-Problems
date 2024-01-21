class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        odds = 0
        subarray_count = 0
        answer = 0
        for right in range(len(nums)):
            if nums[right]%2:
                odds += 1
                subarray_count = 0
            while odds == k:
                if nums[left]%2:
                    odds -= 1
                left += 1
                subarray_count += 1
            answer += subarray_count
        return answer
