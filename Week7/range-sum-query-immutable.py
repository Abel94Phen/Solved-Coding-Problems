class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum_array = []
        prefix_sum = 0
        for i in nums:
            prefix_sum += i
            self.prefix_sum_array.append(prefix_sum)
    def sumRange(self, left: int, right: int) -> int:
        leftSum = self.prefix_sum_array[left - 1] if left > 0 else 0
        rightSum = self.prefix_sum_array[right]
        return rightSum - leftSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)