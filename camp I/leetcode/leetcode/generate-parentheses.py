class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result=[]
        def backtrack(opening_count,closing_count,curr):

            if opening_count == closing_count == n:
                result.append(''.join(curr))
                
            if opening_count < n:
                curr.append('(')
                backtrack(opening_count + 1,closing_count,curr)
                curr.pop()
                
            if closing_count < opening_count:
                curr.append(')')
                backtrack(opening_count,closing_count + 1,curr)
                curr.pop()
                
                
        backtrack(0,0,[])   
        
        return result
        
                            
                