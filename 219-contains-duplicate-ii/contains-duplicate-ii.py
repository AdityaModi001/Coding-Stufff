class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        n = len(nums)       
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         if nums[i] == nums[j] and abs(i-j) <= k:
        #             return True 
        
        # return False

        hashset = set()
        for i in range(n):
            if nums[i] in hashset:
                return True 
            hashset.add(nums[i])

            if len(hashset) > k:
                hashset.remove(nums[i-k])
        
        return False