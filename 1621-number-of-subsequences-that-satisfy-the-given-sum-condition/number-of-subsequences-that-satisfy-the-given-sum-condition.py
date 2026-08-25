class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        MOD = 10**9 + 7 
        num_of_subseq = 0
        left = 0 
        right = len(nums) - 1
        nums.sort()
        while left <= right:

            if nums[left] + nums[right] <= target:
                num_of_subseq += pow(2, right - left, MOD)
                left += 1

            else:
                right -= 1 

        return num_of_subseq % MOD 
