class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        LEN = len(nums1)
        # j = 0 
        # to_start = LEN - n
        # for i in range(1,LEN):
        #     if nums1[i+1] < nums2[i]:
        #         continue 
        #     nums1[i], nums2[j] = nums2[j],nums1[i]
        

        # for j in range(n):
        #     nums1[m+j] = nums2[j]
        # nums1.sort()

        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        return nums1