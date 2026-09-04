class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        instability_score_idx = -1
        min_idx = float('inf')
        i = 0 
        n = len(nums)
        while i < n:
            max_ele = max(nums[0:i+1])
            min_ele = min(nums[i:n])
            score = max_ele - min_ele 
            if score <= k and instability_score_idx < min_idx:
                instability_score_idx = i
                min_idx = instability_score_idx

            i += 1
    
        return instability_score_idx
            


