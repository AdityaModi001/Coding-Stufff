import sys 
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        n = len(nums)
        oper = n - 1 
        count = 0
        # while len(set(nums)) != 1:
        #     max_ele = max(nums)
        #     for i in range(oper):
        #         if nums[i] != max_ele:
        #             nums[i] += 1
        #     print(nums)
        #     count +=1 
    
        # return count
        Sum = 0
        min_ele = min(nums)
        for i in range(n-1,-1,-1):
            Sum += nums[i] - min_ele
    
        return Sum