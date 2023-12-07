class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        path_length = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            if abs(ghost[0]-target[0]) + abs(ghost[1]-target[1]) <= path_length:
                return False
        return True