class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # instability_idx = -1 
        # n = len(nums)
        # for i in range(n):
        #     max_ele = max(nums[0:i+1])
        #     # Use a conditional expression to prevent ValueError when the right slice is empty
        #     min_ele = min(nums[i+1:n]) if i+1 < n else nums[i]

        #     if max_ele - min_ele <= k:
        #         instability_idx = i 
        
        # return instability_idx

        n = len(nums)
        if n == 0:
            return -1

        # Step 1: Precompute prefix maximums
        prefix_max = [0] * n
        current_max = nums[0]
        for i in range(n):
            current_max = max(current_max, nums[i])
            prefix_max[i] = current_max
    
        suffix_min = [0] * n
        current_min = nums[-1]

        for i in range(n - 1, -1, -1):
            current_min = min(current_min, nums[i])
            suffix_min[i] = current_min

        instability_idx = -1
        for i in range(n):
            if prefix_max[i] - suffix_min[i] <= k:
                return i
                

        return instability_idx



