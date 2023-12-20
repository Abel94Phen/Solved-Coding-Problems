class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        pos = len(digits) - 1
        incremented = False
        
        while  pos > -1:
            if digits[pos] + 1 == 10:
                digits[pos] = 0
                pos -= 1
            
            else:
                digits[pos] += 1
                incremented = True
                break
        if not incremented:
            digits.insert(0,1)
        
        return digits