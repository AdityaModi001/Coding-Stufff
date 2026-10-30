class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        # nums.sort()
        # for i in range(n):
        #     if nums[i] > 0:
        #         idx = i
        #         break
        # nums_sum = 0
        # f_sum = 1
        # for i in range(idx,n):
        #     nums_sum += nums[i]
        # for i in range(1,n+1):
        #     f_sum += i
        # return sum(nums)
        # return f_sum - nums_sum

        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(n):
                val = abs(nums[i])
                if 1 <= val <= n:
                    if nums[val - 1] > 0:
                        nums[val - 1]*= -1
                    elif nums[val-1] == 0:
                        nums[val - 1] = -1 * (n+1)
        
        for i in range(1,n+1):
            if nums[i - 1] >= 0:
                return i 
        return n +1

        