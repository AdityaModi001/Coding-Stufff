class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        n = len(boxes)
        ans = [0] * n 
        # 0 if the ith box is empty
        # else 1 if not and contains one ball
        
        # adjacent cond: abs(i-j) == 1
        # operations= 0
        for i in range(n): # i = 0 
            operations =0 
            for j in range(n):
                if boxes[j] == '1':
                    operations += abs(i - j)
            ans[i] = operations

        return ans  
