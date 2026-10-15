import sys
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0 
        val = 0
        for i in range(n):
            for j in range(i,n):
                val = len(set(nums[i:j+1]))
                count += val**2
        
        return count