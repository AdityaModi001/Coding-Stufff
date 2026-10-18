import sys 
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        def calcualtion(operand):
            if tokens[i] == '+':
                f = stack.pop()
                s = stack.pop()
                res = s + f 
                stack.append(res)

            elif tokens[i] == '-':
                f = stack.pop()
                s = stack.pop()
                res = s - f 
                stack.append(res)

            elif tokens[i] == '*':
                f = stack.pop()
                s = stack.pop()
                res = f * s 
                stack.append(res)

            elif tokens[i] == '/':
                f = stack.pop()
                s = stack.pop()
                res = s / f
                stack.append(int(res))
        stack = []
        n = len(tokens)
        for i in range(n):
            res = 0 
            if tokens[i] != '+' and tokens[i] != '-' and tokens[i] != '*' and tokens[i] != '/':
                stack.append(int(tokens[i]))
                
            else:
                calcualtion(tokens[i])
        return stack[-1]
                    