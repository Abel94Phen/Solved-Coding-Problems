class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        t_window = dict(Counter(t))
        window = dict()
        got, required = 0, len(t_window)
        result, length = [-1, -1], len(s) + 1
        left = 0

        for right in range(len(s)):
            character = s[right]
            window[character] = 1 + window.get(character, 0)

            if character in t_window and window[character] == t_window[character]:
                got += 1
            
            while got == required:
                if (right - left + 1) < length:
                    result = [left, right]
                    length = right - left + 1
            
                window[s[left]] -= 1
                if s[left] in t_window and window[s[left]] < t_window[s[left]]:
                    got -= 1
                left += 1
            
        return s[result[0] : result[1] + 1] if length != len(s) + 1 else ""
                