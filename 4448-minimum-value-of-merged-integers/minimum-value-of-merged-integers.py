class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        n = len(nums)
        s = ""
        Min = float('inf')
        for i in range(0,n-1,2):
            s = ''
            s += str(nums[i]) + str(nums[i+1])
            if int(s) < Min:
                Min  = int(s)
                
        return Min