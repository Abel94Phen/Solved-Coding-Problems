class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        def reverse(number):
            reversed_number = 0
            while number:
                reversed_number = reversed_number*10 + number%10
                number //= 10
            return reversed_number
        hashset = set(nums)
        for num in nums:
            reversed_num = reverse(num)
            if reversed_num not in hashset:
                hashset.add(reversed_num)
        return len(hashset)
