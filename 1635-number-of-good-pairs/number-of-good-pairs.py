class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count_good_paris = 0 
        i = 0 
        while i < n - 1:
            for j in range(i+1,n):
                if nums[i] == nums[j]:
                    count_good_paris += 1
            i += 1

        return count_good_paris