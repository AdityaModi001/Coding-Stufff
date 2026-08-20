class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res = []
        n = len(nums)
        for i in range(n):
            if nums[i] < pivot:
                res.append(nums[i])
        for i in range(n):
            if nums[i] == pivot:
                res.append(nums[i])
        for i in range(n):
            if nums[i] > pivot:
                res.append(nums[i])

        return res