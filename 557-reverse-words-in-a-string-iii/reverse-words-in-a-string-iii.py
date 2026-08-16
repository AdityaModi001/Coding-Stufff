class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        res = ""
        # return s
        n = len(s)
        for word in s:
            left = len(word) - 1
            while left >= 0:
                res += word[left]
                
                left -= 1
            res += " "
        
        return res.strip()


        