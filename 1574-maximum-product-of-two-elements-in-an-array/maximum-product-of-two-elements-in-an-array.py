class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MAX = 0 
        n = len(nums)
            # i = 1,2,3,4
            # j = 1,2,3,4
            # (1,2)(1,3)(1,4)
            # [3, 4, 5, 2]
        for i in range(n):
            for j in range(i+1,n):
                curr_pro = (nums[i] - 1) * (nums[j] -1)
                if curr_pro > MAX:
                    MAX = curr_pro
        
        return MAX