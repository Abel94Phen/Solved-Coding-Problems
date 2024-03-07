class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # This needs improvement
        directions = {0 : (0, 1), 1 : (-1, 0), 2 : (0, -1), 3 : (1, 0)}
        pointer = 0
        current = [0, 0]
        for instruction in instructions:
            if instruction == 'G':
                current[0] += directions[pointer%4][0]
                current[1] += directions[pointer%4][1]
            else:
                pointer = pointer - 1 if instruction == 'L' else pointer + 1
        return current == [0, 0] or (pointer%4)
            
