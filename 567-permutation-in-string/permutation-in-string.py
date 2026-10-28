import sys 
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # n1 = len(s1)
        # ascii_sum = 0 
        # for i in s1:
        #     ascii_sum += ord(i)

        # print("required sum",ascii_sum)
        # n2 = len(s2)
        # i = 0 
        # while i <= n2 - n1:
        #     curr_sum = 0 
        #     for j in range(i,i+n1):
        #         curr_sum += ord(s2[j])
        #     print('after cal',curr_sum)
        #     if curr_sum == ascii_sum:
        #         return True 
        #         break

        #     i += 1
        
        # return False

        # s1_count = [0] * 26
        # s2_count = [0] * 26

        # # Initialize the frequency count for s1 and the first window in s2
        # for i in range(len(s1)):
        #     s1_count[ord(s1[i]) - ord('a')] += 1
        #     s2_count[ord(s2[i]) - ord('a')] += 1
    
        # print(s1_count)
        # print(s2_count)

        n1 = len(s1)
        n2 = len(s2)

        freq1 = Counter(s1)
        freq2 = Counter(s2[:n1])

        i = 0 
        j = n1 - 1
        while j < n2 - 1:
            if freq1 == freq2:
                return True 
            
            freq2[s2[i]] -= 1
            i += 1

            j += 1
            freq2[s2[j]] = freq2.get(s2[j],0) +1 
        
        return freq1 == freq2 
        
