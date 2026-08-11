class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 0 index intitger array numa
        # n = len(nums)
        # pref_sum_array = [nums[0]]
        # for i in range(1,n):
        #     j = i 
        #     if nums[j-1] + 1 in nums:
        #         pref_sum_array.append(nums[j])
        #     else:
        #         break
        # # return pref_sum_array
        # res = sum(pref_sum_array)
        # while True:
        #     if res not in nums:
        #         return res
        #         break
        #     else:
        #         res += 1
        
        # return res     
        pref_arr = [nums[0]]
        n = len(nums)
        for i in range(1,n):
            j = i 
            if nums[j] != nums[j-1] + 1:
                break
            else:
                pref_arr.append(nums[j])
            # else:
            #     break
        # return pref_arr
        res = sum(pref_arr)
        x = res
        while True:
            if x not in nums:
                return x
                break
            else:
                x += 1
        
        return x


            