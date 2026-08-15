class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        s = ""
        n = len(word1)
        m = len(word2)

        i = 0
        j = 0

        while i < n and j < m:
            s += word1[i] + word2[j]
            i += 1
            j += 1

        if i < n:
            s += word1[i:n]

        if j < m:
            s += word2[j:m]

        return s