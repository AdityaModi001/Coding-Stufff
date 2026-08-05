class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        res = []
        s1 = s1.split()

        # s1  = s1.strip()
        # return s1
        s2 = s2.split()
        # return s1
        for i in s1:
            if i not in s2 and s1.count(i) == 1:
                res.append(i)
        for i in s2:
            if i not in s1 and s2.count(i) == 1:
                res.append(i)
        
        return res

