class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def predict(l,r):
            if l > r:
                return 0
            else:
                left = nums[l] - predict(l + 1, r)
                right = nums[r] - predict(l, r - 1)
                return max(left, right)
        
        return predict(0, len(nums) - 1) >= 0
        