class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def swapper(s, index):
            if index == len(s)//2:
                return
            else:
                s[index],s[len(s) - index - 1] = s[len(s) - index - 1], s[index]
                swapper(s, index + 1)

        swapper(s, 0)