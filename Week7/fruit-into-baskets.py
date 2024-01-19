class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_count = {}
        left = 0
        max_count = 0
        for right in range(len(fruits)):
            fruit_count[fruits[right]] = 1 + fruit_count.get(fruits[right], 0)
            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1
            max_count = max(max_count, right - left + 1)
            print(fruit_count)
        return max_count