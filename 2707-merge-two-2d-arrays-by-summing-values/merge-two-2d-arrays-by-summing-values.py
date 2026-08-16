from collections import Counter 
class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        freq = {}

        for key, value in nums1:
            freq[key] = value
        for key, value in nums2:
            freq[key] = freq.get(key, 0) + value
        # return freq
        
        result = [[key,value] for key,value in freq.items()]

        result = sorted(freq.items())
        return result