class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq  = {}
        for i in arr:
            freq[i] = freq.get(i,0) +1
        
        max_ele = -1
        for key,val in freq.items():
            if key == val:
                curr_ele = key
                max_ele = max(max_ele,curr_ele)
        return max_ele