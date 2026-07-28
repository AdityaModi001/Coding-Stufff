class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # n = len(s)
        # if n == 1:
        #     return s
        # if n ==3:
        #     return s

        # result = "".join(sorted(s[:n//2])) + s[n//2] + "".join(sorted(s[n//2+1:n], reverse=True))


        # return result

        half = len(s) // 2
        start = "".join(sorted(s[:half]))

        if len(s) % 2 != 0:
            mid = s[half]
        else:
            mid = ""

        return start + mid + start[::-1]