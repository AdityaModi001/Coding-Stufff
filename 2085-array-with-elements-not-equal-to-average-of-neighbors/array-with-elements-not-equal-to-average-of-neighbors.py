class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        # n = len(nums)
        # res = [None] * n 
        # j = 1 
        # median = n //2
        # for i in range(n):
        #     if nums[i] < nums[median]:
        #         res[j] = nums[i]
        #         j += 2
        # j = 0 
        # for i in range(n):
        #     if i not in res:  # If this element hasn't been used yet
        #         res[j] = nums[i]
        #         j += 2
                
        # return res

        l = 0 
        res = []
        r = len(nums) - 1
        while len(nums) != len(res):
            res.append(nums[l])
            l +=1
            if l <= r:
                res.append(nums[r])
                r -= 1
        
        return res