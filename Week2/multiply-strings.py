class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        decimals = "0123456789"
        if num1 == '0' or num2 == '0':
            return '0'
        new_num1, new_num2 = 0,0
        for i in range(len(num1)):
            new_num1 = 10*new_num1 + decimals.index(num1[i])
        for i in range(len(num2)):
            new_num2 = 10*new_num2 + decimals.index(num2[i])
        result = new_num1 * new_num2
        string_result = ""
        while result:
            string_result = decimals[result%10] + string_result
            result //= 10
        return string_result