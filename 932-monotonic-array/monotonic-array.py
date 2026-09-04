class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # the question says the array is monotinic of wither it is increaign or decreaing 

        n = len(nums)
        if n == 1:
            return True 

        def Mono_increaing(nums):
            i = 0 
            j = 1 
            while j < n:
                if nums[i] <= nums[j]:
                    i += 1
                    j += 1
                else:
                    return False
            return True 

        def mono_decreaing(nums):
            # nums[i] >= nums[j]
            j = 1 
            i = 0 
            while j < n:
                if nums[i] >= nums[j]:
                    i += 1
                    j += 1
                else:
                    return False

            return True 
        
        if nums[0] <= nums[1]:
            Mono_increaing(nums)

        else:
            mono_decreaing(nums)
        
        return Mono_increaing(nums) or mono_decreaing(nums)

        
            