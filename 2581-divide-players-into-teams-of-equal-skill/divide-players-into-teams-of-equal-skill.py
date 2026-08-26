class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        # skills is of even length 
        # skill[i] denotes the skill of ith player 
        # res1 = []
        # res2 = []
        # n = len(skill)
        # for i in range(n//2):
        #     res1.append(skill[i])
        # for i in range(n//2,n):
        #     res2.append(skill[i])

        # res = [] 
        # for i in res1:
        #     for j in res2:
        #         res.append(i+j)
    
        # return res
        chemistry = 0
        skill.sort()
        left = 0 
        right = len(skill) - 1
        total_skill = skill[left] + skill[right]
        while left < right:
            curr_sum =  skill[left] + skill[right]
            if curr_sum != total_skill:
                return -1 
            chemistry += skill[left] * skill[right]
            left += 1 
            right -= 1


        return chemistry

