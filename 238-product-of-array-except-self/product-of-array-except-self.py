class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # n = len(nums)
        # ans = [0]*n
        1, 2,  6,  24
        4, 12, 24, 24
        # def helper_prefix(prefix_arr):
        #     if prefix_arr == []:
        #         return 1 

        #     product1 = 1
        #     for i in range(len(prefix_arr)):
        #         product1 = product1*prefix_arr[i]
        #     return product1
        # def helper_suffix(suffix_arr):
        #     product2 = 1
        #     if suffix_arr == []:
        #         return 1

        #     for i in range(len(suffix_arr)):
        #         product2 = product2*suffix_arr[i]

        #     return product2




        # for i in range(n):
        #     prefix_arr = nums[0:i]
        #     suffix_arr = nums[i+1:n]
        #     # return prefix_arr
            
        #     pre = helper_prefix(prefix_arr)
        #     suf = helper_suffix(suffix_arr)
        #     ans[i] = pre * suf
        # return ans

        n = len(nums)
        prefix = 1
        result = [1] * n 
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(n-1,-1,-1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result