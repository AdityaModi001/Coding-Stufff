class Solution:
    def maxProduct(self, n: int) -> int: # 31
        max1 = max2 = 0 
        while n:
            d = n % 10 # 1
            if d >= max1:
                max2 = max1 # max2 = 0 
                max1 = d # max1 = 1
            elif d > max2:
                max2 = d
            n //= 10 
        
        return max1 * max2 