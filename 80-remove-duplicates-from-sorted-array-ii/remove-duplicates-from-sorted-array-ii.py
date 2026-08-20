class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # each unique elemnt should apper at most twice 
            # n = len(nums)
            # l =1 
            # for r in range(1, n):
            #    if nums[r] != nums[r - 1]:
            #        nums[l] = nums[r]
            #        l += 1 vcoiu       
            # return l



        n = len(nums)
        l = 2
        for i in range(2,n):
            if nums[i] != nums[l-2]:
                nums[l] = nums[i]
                l += 1
        return l
        