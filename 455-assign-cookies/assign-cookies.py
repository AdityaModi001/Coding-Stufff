class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # to give each child at most 1 cookies
        # each child i has a greed factor of g[i]
        count_child_content =  0 

        n = len(g) # len of children 
        m = len(s) # len of the cookies 
        i = 0
        j = 0 
        g.sort()
        s.sort()
        # for i in range(n):
        #     if s[j] >= g[i]:
        #         count_child_content += 1
        #         s[j],s[i] = -1,-1
        #         j += 1


        # return count_child_content

        while i < len(s) and j < len(g):
            if g[j] <= s[i]:
                j += 1
            i += 1
        
        return j