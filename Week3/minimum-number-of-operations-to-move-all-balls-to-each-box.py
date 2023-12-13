class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = [0 for _ in range(len(boxes))]
        left_count, left_move = 0, 0
        for i in range(1, len(boxes)):
            if boxes[i-1] == '1': left_count += 1
            left_move += left_count
            result[i] = left_move
        
        right_count, right_move = 0, 0
        for i in range(len(boxes)-2, -1, -1):
            if boxes[i+1] == '1': right_count += 1
            right_move += right_count
            result[i] += right_move
        
        return result