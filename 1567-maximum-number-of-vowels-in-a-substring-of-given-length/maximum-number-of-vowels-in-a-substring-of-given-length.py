class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        d = {'a','e','i','o','u'}
        i , j = 0 , 0 
        max_count = 0 
        count = 0 
        while j < n:
            if s[j] in d:
                count += 1
            if (j - i + 1 == k):
                max_count  = max(max_count, count)
                if s[i] in d:
                    count -= 1
                i += 1
            j += 1

        return max_count 