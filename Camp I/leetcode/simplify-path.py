class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        print(path)
        stack = []
        for string in path:
            if stack and string == '..':
                stack.pop()
            elif string == '' or string == '.' or string == '..':
                continue
            else:
                stack.append(string)
        return '/' + '/'.join(stack)