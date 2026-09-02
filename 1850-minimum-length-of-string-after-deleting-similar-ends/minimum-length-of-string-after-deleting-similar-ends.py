class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = ""
        n = len(s)
        if n == 1:
            return 1

        i = 0 
        j = n - 1
        # while i <= j:
        #     if s[i] == s[j]:
        #         if i == j:
        #             res += s[i]
        #         else:
        #             res += s[i] * 2
        #         i += 1
        #         j -= 1
        #     elif res and s[i] == res[-1]:
        #         i += 1
        #     elif res and s[j] == res[-1]:
        #         j -= 1
        #     else:
        #         break
            
        # return n - len(res)
            

        while i < j and s[i] == s[j]:
            match = s[i]

            while i <= j and s[i] == match:
                i += 1
            while i <= j and s[j] == match:
                j -= 1


        return j - i + 1 

