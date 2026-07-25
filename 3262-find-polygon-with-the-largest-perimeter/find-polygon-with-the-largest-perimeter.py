class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        res =[]
        nums.sort()
        n = len(nums)
        Sum = 0

        for i in range(n - 1):
            Sum += nums[i]
            if Sum > nums[i + 1]:
                res.append(Sum + nums[i + 1])

        return max(res) if res else -1
        
            
        