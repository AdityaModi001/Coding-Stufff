import sys 
class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        push_stack = []
        n = len(pushed)
        m   = len(popped)
        j =  0
        for i in range(n):
            push_stack.append(pushed[i])
            while j < m:
                if push_stack and push_stack[-1] == popped[j]:
                    push_stack.pop()
                    j += 1
                else:
                    break
                    

        if not push_stack:
            return True 
        return False

