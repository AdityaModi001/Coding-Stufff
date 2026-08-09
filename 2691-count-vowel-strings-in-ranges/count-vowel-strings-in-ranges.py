class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # given: string and 2d array queries 
        # to find out the strings present over the index [l1 and ri] that start and ends with voewl 
        # ans  = [] 
        # count =0 
        # vowels = ['a', 'e', 'i', 'o','u']
        # for i in queries:
        #     count = 0 
        #     start = i[0] # 0
        #     end = i[-1] # 2
        #     j = start # j = 0
        #     while j < end+1: # j = 0,1,2
        #         if words[j][0] in vowels and words[j][-1] in vowels:
        #             count += 1
        #         # else:
        #         #     count =0 
        #         j += 1
                
        #     ans.append(count)
                
        
        # return ans

        # pre computing the total prefix sum 
        vowels = {'a', 'e', 'i', 'o', 'u'}

        prefix_count = 0
        total_number_of_prefix_sum = [0]
        ans = []

        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                prefix_count += 1

            total_number_of_prefix_sum.append(prefix_count)

        for query in queries:
            l = query[0]
            r = query[1]

            res = total_number_of_prefix_sum[r + 1] - total_number_of_prefix_sum[l]
            ans.append(res)

        return ans