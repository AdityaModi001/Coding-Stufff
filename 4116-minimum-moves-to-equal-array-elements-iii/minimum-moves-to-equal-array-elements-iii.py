class Solution:
    def minMoves(self, nums: List[int]) -> int:
        Max = max(nums)
        n = len(nums)
        count = 0 
        for i in range(n):
            count += abs(Max - nums[i])
        
        return count