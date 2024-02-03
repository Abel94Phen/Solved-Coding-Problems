class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sub_sum = sum(arr[:k])
        count = 0
        left = 0
        if sub_sum / k >= threshold:
                count += 1
        for right in range(k, len(arr)):
            sub_sum -= arr[left]
            left += 1
            sub_sum += arr[right]
            if sub_sum / k >= threshold:
                count += 1
        return count