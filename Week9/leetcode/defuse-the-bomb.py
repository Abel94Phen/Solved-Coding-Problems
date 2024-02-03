class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = [0] * len(code)
        for i in range(len(code)):
            if k > 0:
                total = 0
                for x in range(1, k + 1):
                    total += code[(i + x) % len(code)]
                result[i] = total
            elif k < 0:
                total = 0
                for x in range(1, -k + 1):
                    total += code[(i - x) % len(code)]
                result[i] = total
            else:
                result[i] = 0

        
        return result