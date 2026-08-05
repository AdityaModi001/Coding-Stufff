class Solution(object):
    def strStr(self,haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # to return the first occurrence of needle in haystack
        # first_occurrence = 0 
        count_similar =0 
        res = []
        n = len(haystack)
        m = len(needle)
    
        
        # for i in range(0,n-1):
        #     while j < m:
        #         if haystack[i] == needle[j]:
        #             count_similar += 1
        #             j += 1
        #             break
        #         if count_similar == 3:
        #             res.append(n - i)
        #     else:
        #         j = 0 
        for i in range(n-m+1):
            j = 0
            while j < m:
                if haystack[i + j] != needle[j]:
                    break
                j += 1
            if j ==m:
                return i
        
        return -1 

                    
