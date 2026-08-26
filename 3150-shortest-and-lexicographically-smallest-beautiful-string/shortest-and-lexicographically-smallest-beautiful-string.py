import math
class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        max_ = float('inf')
        max_len = 102
        res = []
        # count_1 == k
        n = len(s)
        i = 0 
        while i < n:
            count_1s = 0 
            for j in range(i,n):
                if s[j] == '1':
                    count_1s += 1
                    if count_1s == k and int(s[i:j]+s[j]) < max_ and len(s[i:j]) <= max_len:
                        max_ = int(s[i:j] + s[j])
                        max_len = len(s[i:j])
                        
            i += 1
        
        # if max_ == "inf":
        #     return ""
        # else:
        

# Use this if max_ = float('inf')
        if math.isinf(max_):
            return ""
        return str(max_)
        # return res
        # return max_
        # if max_ == "inf":
        #     return ""
        # [6,8,7,6,5]
        # min = float('inf')
        # for i in res:
        #     if len(i) < min:
        #         min = len(i)

        # for i in res:
        #     if len(i) == min:
        #         return i

        # if r
        
        # res1 = 
