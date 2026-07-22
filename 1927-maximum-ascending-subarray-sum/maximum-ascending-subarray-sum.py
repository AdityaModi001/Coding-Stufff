class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = 0 
        curr_sum =0 
        if n == 1:
            return nums[0]

        curr_sum = nums[0]
        max_sum = curr_sum 

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                curr_sum += nums[i]
            else:
                curr_sum = nums[i]

            max_sum = max(curr_sum, max_sum)
        
        return max_sum


