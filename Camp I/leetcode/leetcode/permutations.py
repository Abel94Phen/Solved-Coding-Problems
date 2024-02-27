class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        if len(nums) == 1: return [nums[:]]
        
        for i in range(len(nums)):
            x = nums.pop(0)
            permutations = self.permute(nums)
            
            for perm in permutations:
                perm.append(x)
            result.extend(permutations)
            nums.append(x)

        return result