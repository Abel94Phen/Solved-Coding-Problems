class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            if i not in seen:
                cycle = set()
                while True:
                    if i in cycle:
                        return True
                    seen.add(i)
                    cycle.add(i)
                    prev, i = i, (i + nums[i])%len(nums)
                    if prev == i or nums[prev] > 0 != nums[i] < 0:
                        break
        return False