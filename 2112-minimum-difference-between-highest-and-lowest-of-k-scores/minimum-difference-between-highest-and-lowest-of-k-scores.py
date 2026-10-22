class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        maxx = float('inf')
        to_iterate = n - k + 1
        i = 0 
        while i < to_iterate:
            res = []
            for j in range(i,i+k):
                res.append(nums[j])
            
            min_ele = min(res)
            max_ele = max(res)
            if max_ele - min_ele <= maxx:
                maxx = max_ele - min_ele
        
            i += 1 
    
        return maxx