class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        valid = True 
        count =0 
        for i in range(len(arr1)):
            arr1_valid = True 
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    arr1_valid = False
            if arr1_valid:
                count+=1
        return count