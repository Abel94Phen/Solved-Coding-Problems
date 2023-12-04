class Solution:
    def printVertically(self, s: str) -> List[str]:
        listed_string = s.split()
        word_length = 0
        for i in listed_string:
            if len(i) > word_length:
                word_length = len(i)
        
        result = ["" for _ in range(word_length)]
        
        
        for i in range(len(listed_string)):
            for j in range(len(result)):
                if j >= len(listed_string[i]):
                    result[j] += " "
                else:
                    result[j] += listed_string[i][j]
        
        for i in range(word_length):
            result[i] = result[i].rstrip()
                
            
        return result
        
        """
         C I C
         O S O
         N   M
         T   I
         E   N
         S   G
         T
         I S
         
        
        """
        
        