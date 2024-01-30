class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_list, t_list = list(s), list(t)
        s_list.sort()
        t_list.sort()
        for _ in range(len(s)):
            if s_list[_] != t_list[_]:
                return t_list[_]
        return t_list[-1]