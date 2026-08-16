class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return [nums[0]]
        i = 0 
        j = n - 1
        while i < j:
            if nums[i] % 2 == 0:
                i += 1
            elif nums[j] % 2 != 0:
                j -= 1
            else:
                nums[i] , nums[j] = nums[j] , nums[i]
                i +=1 
                j -= 1
        
        return nums        