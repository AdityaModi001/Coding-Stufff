class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 1. Count the frequency of each number
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            
        # 2. Sort the items by their value (frequency) in descending order
        # x[1] ensures we sort by the count, NOT the number itself
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        # 3. Extract only the keys (the original numbers) from the top k items
        return [item[0] for item in sorted_items[:k]]
