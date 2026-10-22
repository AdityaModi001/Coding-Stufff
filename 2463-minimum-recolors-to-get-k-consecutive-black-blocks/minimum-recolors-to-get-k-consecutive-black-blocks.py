import sys 
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        # if n > k:
        #     return 0
        # if "B"*k in blocks:
        #     return 0 
        '''
        3,4
        '''
        to_iterate = n - k + 1
        final_min_w = float('inf')
        i = 0 
        count_w = 0
        while i < to_iterate:
            count_w = 0
            for j in range(i,i+k):
                if blocks[j] == 'W':
                    count_w += 1
            if count_w < final_min_w:
                   final_min_w = count_w
            i += 1
        return final_min_w