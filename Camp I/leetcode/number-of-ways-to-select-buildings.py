class Solution:
    def numberOfWays(self, s: str) -> int:
        zero_count, one_count = s.count('0'), s.count('1')
        start_zero, start_one = 0, 0
        ways = 0

        for char in s:
            if char == '0':
                ways += start_one * (one_count - start_one)
                start_zero += 1
            else:
                ways += start_zero * (zero_count - start_zero)
                start_one += 1
        return ways
