class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x,y = nums[0:n], nums[n:]
        nums = []
        for i in range(n):
            nums.append(x[i])
            nums.append(y[i])
        return nums