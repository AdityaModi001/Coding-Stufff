class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n ==1:
            return nums
        count = Counter(nums)
        def custom_sort(n):
            return (count[n], -n)
        nums.sort(key = custom_sort)
    
        return nums
