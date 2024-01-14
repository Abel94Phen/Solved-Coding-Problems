class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [['g' for i in range(n)] for i in range(m)]
        for guard in guards:
            matrix[guard[0]][guard[1]] = 'G'
        for wall in walls:
            matrix[wall[0]][wall[1]] = 'W' 
        
        '''
        matrix = [['G','W','g','g','g','g'],
                  ['g','G','g','g','W','g'],
                  ['g','g','W','G','g','g'],
                  ['g','g','g','g','g','g']]
        wanted to match the picture

        'G' = Guard
        'W' = Wall
        'g' = green, not seen by guard
        'r' = red, seen by guard
        '''

        count = 0
        for x,y in guards:
            if x > 0: # checks left of the current guard
                for j in range(x-1,-1,-1):
                    curr = matrix[j][y]
                    if curr == 'W' or curr == 'G':
                        break
                    else:
                        matrix[j][y]='r'

            if x < m-1:
                for j in range(x+1,m):
                    curr = matrix[j][y]
                    if curr == 'W' or curr == 'G':
                        break
                    else:
                        matrix[j][y]='r'
            
            if y > 0:
                for j in range(y-1,-1,-1):
                    curr = matrix[x][j]
                    if curr == 'W' or curr == 'G':
                        break
                    else:
                        matrix[x][j]='r'
            
            if y < n-1:
                for j in range(y+1,n):
                    curr = matrix[x][j]
                    if curr == 'W' or curr == 'G':
                        break
                    else:
                        matrix[x][j]='r'
        
        for i in matrix:
            for j in i:
                if j == 'g':
                    count += 1       
        return count