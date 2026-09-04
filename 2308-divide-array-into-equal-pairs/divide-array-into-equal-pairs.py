class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        to_check = list(set(nums))

        for i in range(len(to_check)):
            count =0  
            for j in range(len(nums)):
                if to_check[i] == nums[j]:
                    count += 1
            if count % 2 != 0:
                return False
        
        return True