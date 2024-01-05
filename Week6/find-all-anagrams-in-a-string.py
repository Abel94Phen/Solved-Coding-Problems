class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        p_dic = dict(collections.Counter(p))
        s_dic = dict(collections.Counter(s[:len(p)]))
        result = []
        if s_dic == p_dic:
            result.append(0)
        for i in range(len(s) - len(p)):
            s_dic[s[i]] -= 1
            if s_dic[s[i]] == 0:
                del s_dic[s[i]]
            s_dic[s[i + len(p)]] = s_dic.get(s[i + len(p)], 0) + 1
            
            if s_dic == p_dic:
                result.append(i + 1)

        return result