class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums[0] % 2 == 0:
            prev = "Even"
        else:
            prev = "odd"
        for i in range(1,len(nums)):

            if nums[i] % 2 == 0:
                curr = "Even"
            else:
                curr = "odd"
            # return curr
            if curr == prev:
                return False
            else:
                prev = curr 
        
        return True 
