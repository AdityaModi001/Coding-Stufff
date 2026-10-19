import sys
class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        n = len(asteroids)
        '''
        5     10     -5 

        0      1      2
        '''
        # stack = []
        # for i in range(n):
        #     stack.append()
        n = len(asteroids)
        stack = []
        for i in range(n):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            else:
                while len(stack) != 0 and stack[-1] > 0 and stack[-1] < abs(asteroids[i]):
                    stack.pop()
                
                if len(stack) != 0 and stack[-1] == abs(asteroids[i]): 
                    stack.pop()
                elif len(stack) == 0 or stack[-1] < 0:
                    stack.append(asteroids[i])
        
        return stack