class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count_array = [0 for _ in range(max(nums) + 1)]
        sorted_nums = []
        result = []

        for num in nums:
            count_array[num] += 1
        
        for i in range(len(count_array)):
            while count_array[i] > 0:
                sorted_nums.append(i)
                count_array[i] -= 1
        
        for num in nums:
            result.append(sorted_nums.index(num))

        return result