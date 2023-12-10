class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        op_dic = {num:i for i,num in enumerate(nums)}
        
        for operation in operations:
            index = op_dic[operation[0]]
            nums[index] = operation[1]
            op_dic[operation[1]] = index
            del op_dic[operation[0]]
        return nums