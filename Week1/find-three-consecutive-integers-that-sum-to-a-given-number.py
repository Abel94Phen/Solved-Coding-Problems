class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        """
        result_array = []
        numbers_array = [i+1 for i in range(num+1)]
        i,val = 0,0
        while i <= num-1:
            if sum(numbers_array[i:i+3]) == num:
                break
            i += 1
        return numbers_array[i:i+3]
        
        (x + x+2)/2 * 3 = num
        (2x + 2) * 3 = num
        2x + 2 = (num/3) * 2
        x + 1 == (num/3) * 2
        """
        if num % 3 == 0:
            return [num//3 - 1,num // 3, num//3 + 1]
        else:
            return []
            
    
        
        
        
        
        
            
        