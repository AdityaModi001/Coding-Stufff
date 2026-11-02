class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        number = nums[n//2]
        Sum = 0
        for i in range(n):
            if nums[i] != number:
                Sum += abs(number - nums[i])

        
        return Sum
