class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""
        
        while stack:
            s[stack.pop()] = ""
        
        return "".join(s)










        # res = ""
        # n = len(s)
        # count= 0
        # new_point = 0 

        # for i in range(n):
        #     if s[i] != "(" or s[i] != "(":
        #         point = i   # point = 7
        #     if s[i] == '(':
        #         count += 1 # count = 2
        #         new_point = i # new_point = 3

        #     if s[i] == ')':
        #         count -= 1 # count = 0
        #         new_point = i 
            
        # if count ==0:
        #     res += s[point:n]
        # elif count > 0 or count < 0:
        #     res += s[point:new_point-1]
        
        # return res