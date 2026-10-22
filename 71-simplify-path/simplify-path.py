import sys 
class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split('/')
        n = len(s)
        print("This is the current directory!!!",s)
        stack = []
        for i in range(n):
            if s[i] == '' or s[i] == '.':
                continue
            elif s[i] == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(s[i])
        return '/' + '/'.join(stack)

        #     if not stack:
        #         stack.append('/')
        #     elif i < n - 1 and stack[-1] != '/':
        #         stack.append('/')
        # res = "".join(stack)
        # if len(res) > 1 and res[-1] == '/':
        #     res = res[:-1]
            
        # return res