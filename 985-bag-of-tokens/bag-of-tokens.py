class Solution(object):
    def bagOfTokensScore(self, token, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        token.sort()
        n = len(token)
        score =0 
        max_score = 0 
        idx  = -1
        # val = []
        # for i in range(n):
        #     if power >= token[i]:
        #         power = power - token[i]
        #         score += 1
        #         val.append(token[i])
        #         idx = i 
        #         max_score = score
                
        # if len(val) == len(token):
        #     return max_score
        
        # elif max_score > 0:
        #         max_ele = token[-1]
        #         power = power + max_ele
        #         score = max_score - 1
        #         for j in range(n):
        #             if power >= token[j]:
        #                 power -= token[j]
        #                 score += 1
        #         if max_score > score:
        #             return max_score
                

        # return score


        # token.sort()
        # n = len(token)
        # score = 0
        # max_score = 0
        # idx = -1

        i = 0
        j = n - 1

        while i <= j:

            if power >= token[i]:
                power = power - token[i]
                score += 1
                idx = i
                i += 1
                max_score = max(max_score, score)

            elif score > 0:
                max_ele = token[j]
                power = power + max_ele
                score -= 1
                j -= 1

            else:
                break

        return max_score