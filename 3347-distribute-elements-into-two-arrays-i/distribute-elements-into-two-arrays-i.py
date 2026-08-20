class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        '''
        index array is 1 based 
        perform compulsory n operateions 
        if arr1[-1] > arr2[-1] append -> nums[i] to arr1 else: nums2to 
        '''
        n = len(nums)
        if n < 3:
            return nums
        arr1 = [nums[0]]
        arr2 = [nums[1]]


        for i in range(2,n):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        res = arr1 + arr2
        return res
