import sys
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] != "*":
                stack.append(s[i])
            else:
                stack.pop()
        return "".join(stack)