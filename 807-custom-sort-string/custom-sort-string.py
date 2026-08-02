from collections import Counter
class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """

        char_count = Counter(s)  # {"a":1,"c":1,"b":1,"d":1}
        # return char_count['e']
        res = ""
        for i in range(len(order)):
            if order[i] in s:
                if char_count[order[i]] > 1:
                    res += order[i] * char_count[order[i]]
                else:
                    res += order[i]
        
        
        for i in range(len(s)):
            if s[i] not in res:
                if char_count[s[i]] > 1:
                    res += s[i] * char_count[s[i]]
                else:
                    res += s[i]
        return res
