class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # hashset = set(nums)
        for i in range(1,100+2):
            res = k * i
            if res not in nums:
                return res