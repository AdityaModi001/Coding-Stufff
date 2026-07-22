class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        i = 0
        while i <n:
            
            if i == 0:
                left_sum = 0 
            left_sum = sum(nums[0:i])
            right_sum = sum(nums[i+1 : n])
            if left_sum ==right_sum:
                return i 
            else:
                i += 1
        
        return -1
            

