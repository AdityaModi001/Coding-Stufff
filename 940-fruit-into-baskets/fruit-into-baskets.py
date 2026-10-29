class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        # [ 1,1,1, 2,2,2, 3,3,3 ]

        # n = len(fruits)
        # if n < 3:
        #     return 2
        # max_count = float('-inf')
        # f = fruits[0]
        # s = fruits[1]
        # count_f , count_s = 0,0
        # for i in range(2,n):
        #     if fruits[i] == s:
        #         # curr_count += 1
        #         count_f += 1
        #     elif fruits[i] == f:
        #         count_s += 1
        #     else:
        #         t_c = count_f + count_s
        #         if t_c > max_count:
        #             max_count = t_c
        #         f = s 
        #         s = fruits[i]
        #         count_f = count_s 
        #         count_s =  0
        
        # return max_count
        # this is the brute force approach 
        # max_len = 0 
        # n = len(fruits)
        # for i in range(n):
        #     res = set()
        #     for j in range(i,n):
        #         res.add(fruits[j])
        #         if len(res) <= 2:
        #             max_len = max(max_len , j - i + 1)
        #         else:
        #             break
        
        # return max_len


        n = len(fruits)
        l , r , max_len= 0,0,0
        hashmap  = {}
        while r < n:
            hashmap[fruits[r]] =  hashmap.get(fruits[r], 0) + 1
            if len(hashmap) > 2:
                while len(hashmap) > 2:
                    hashmap[fruits[l]] -= 1
                    if hashmap[fruits[l]] == 0:
                        del hashmap[fruits[l]]
                    l +=1
            
            if len(hashmap) <= 2:
                max_len = max(max_len, r - l + 1)
            
            r += 1

        return max_len          