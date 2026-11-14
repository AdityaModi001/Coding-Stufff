import sys
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        
        # [3,1,2,6]
        # [-2,0,-3,-2]
        # [1,3,6,10]

        # for i in range(1,n):
        #     nums[i] += nums[i-1]
        # print(nums)
        min_ele = float('inf')
        # for i in range(n):
        #     if nums[i] > 0 and nums[i] < min_ele:
        #         min_ele = nums[i]
        # if sum(nums) < 0:
        #     return -1
        # if min_ele > 0:
        #     return min_ele 
        # return -1

        # for i in range(n):
        #     count  = 0 
        #     curr_sum = 0 
        #     for j in range(i,n):
        #         curr_sum += nums[i]
        #         if curr_sum > 0 and curr_sum < min_ele and count < r:
        #             min_ele = curr_sum
        #             count += 1
        # print(min_ele)
        # return min_ele

        # res = []
        # for i in range(n-l+1):
        #     SUM = sum(nums[i:i+l])
        #     if SUM > 0:
        #         print('sum',SUM)
        #         res.append(SUM)
        #         # print('l',res)
        # for i in range(n-r+1):
        #     SUM_ = sum(nums[i:i+r])
        #     if SUM_ > 0:
        #         print('SUM_',SUM_)
        #         res.append(SUM_)
        
        # if not res:
        #     return -1 
        # return min(res)


        n = len(nums)
        ans = float('inf')

        for i in range(n):
            s = 0 
            for j in range(i,n):
                s += nums[j]
                length = j - i + 1
                if l <= length <= r and s > 0:
                    ans = min(ans, s)
        
        return -1 if ans == float('inf') else ans