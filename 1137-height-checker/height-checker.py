class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # expected = heights
        # expected.sort()
        # return heights
        # count = 0 
        # for i in range(len(heights)):
        #     if heights[i] != expected[i]:
        #         count += 1
        
        # return count
        expected = heights[:]
        for i in range(len(expected)-1):
            for j in range(len(expected)-i-1):
                if expected[j] > expected[j+1]:
                    expected[j],expected[j+1] = expected[j+1],expected[j]
        count = 0 
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                count += 1
        
        return count