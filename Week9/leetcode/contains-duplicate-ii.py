class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashset = set()
        left = 0
        for right in range(len(nums)):
            if nums[right] in hashset:
                return True
            hashset.add(nums[right])
            while right - left == k:
                hashset.remove(nums[left])
                left += 1
        return False