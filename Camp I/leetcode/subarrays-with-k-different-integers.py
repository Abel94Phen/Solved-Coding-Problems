class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        subarrays = 0
        left_near, left_far = 0, 0
        hashmap = defaultdict(int)
        for right in range(len(nums)):
            hashmap[nums[right]] += 1

            while len(hashmap) > k:
                hashmap[nums[left_near]] -= 1
                if hashmap[nums[left_near]] == 0:
                    del hashmap[nums[left_near]]
                left_near += 1
                left_far = left_near

            while hashmap[nums[left_near]] > 1:
                hashmap[nums[left_near]] -= 1
                left_near += 1

            if len(hashmap) == k:
                subarrays += left_near - left_far + 1
        return subarrays
