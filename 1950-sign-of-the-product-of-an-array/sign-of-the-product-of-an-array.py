class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg_count = 0 
        pos_count =0 

        for i in nums:
            if i < 0:
                neg_count += 1
            elif i > 0:
                pos_count += 1
            
            else:
                return 0

        if neg_count % 2 ==0:
            return 1
        else:
            return -1
        