class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """
        s1 = sentence1.split()
        s2 = sentence2.split()

        if len(s1) < len(s2):
            s1,s2  = s2,s1
        
        start, end = 0,0
        n1 = len(s1)
        n2 = len(s2)

        while start < n2 and s1[start] == s2[start]:
            start += 1

        while end < n2 and s1[n1-end-1] == s2[n2 - end - 1]:
            end += 1
        
        return start + end >= n2

        # first_s1 = s1[0]
        # last_s1 = s1[-1]

        # first_s2  = s2[0]
        # last_s2 = s2[-1]

        # if len(s1) > len(s2):
            
        #     if first_s2 != first_s1 and last_s2 != last_s1:
        #         return False 
        #     else:
        #         return True
        # elif len(s2) > len(s1):
        #     if first_s1 != first_s2 or last_s1 != 
        #         return False 
        #     else:
        #         return True
        # return s2
        # # for i in s1:
        # #     if i not in s2:
        # #         return False
        # # return True

