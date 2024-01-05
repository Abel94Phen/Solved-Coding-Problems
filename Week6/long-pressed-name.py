class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name == typed:
            return True 
        if len(name) > len(typed):
            return False
        
        name_i, typed_i = 0,0
        while typed_i < len(typed):
            if name_i < len(name) and name[name_i] == typed[typed_i]:
                name_i += 1
            else:
                if typed_i == 0 or typed[typed_i] != typed[typed_i - 1]:
                    return False
            typed_i += 1
        return name_i == len(name)
            