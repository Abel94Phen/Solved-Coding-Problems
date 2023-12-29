class Solution:
    def smallestNumber(self, num: int) -> int:
        answer = 0
        digits = list(map(int,str(abs(num))))
        if num > 0:
            digits.sort()
            if digits[0] == 0:
                for i in range(1,len(digits)):
                    if digits[i] != 0:
                        digits[0], digits[i] = digits[i], digits[0]
                        break
            for digit in digits:
                answer = answer * 10 + digit
        else:
            digits.sort(reverse = True)
            for digit in digits:
                answer = answer * 10 + digit
            answer = answer * -1
        return answer