class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        equal = []
        larger = []
        
        for i in nums:
            if i < pivot:
                smaller.append(i)
            elif i > pivot:
                larger.append(i)
            else:
                equal.append(i)
        
        return smaller + equal + larger