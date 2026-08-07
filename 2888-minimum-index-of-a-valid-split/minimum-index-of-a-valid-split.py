from collections import Counter

class Solution(object):
    def minimumIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # condn: their is a one dominant element in the entire array
        # split the index i into 2 arrays
        # the split is only valid if: 0 <= i < n - 1
        # also the subarray 1 and 2 should have the same dominant element
        # n = len(nums)
        # dominant_ele1 = 0
        # dominant_ele2 = 0

        # for i in range(0,n-1):
        #     arr1 = nums[0:i+1]
        #     arr2 = nums[i+1:n]

        #     n1 = len(arr1)
        #     n2 = len(arr2)

        #     freq1 = Counter(arr1)
        #     freq2 = Counter(arr2)

        #     top_pair1 = freq1.most_common(1)[0]
        #     top_pair2 = freq2.most_common(1)[0]

        #     max_key1 = top_pair1[0]
        #     max_value1 = top_pair1[1]
            
        #     max_key2 = top_pair2[0]
        #     max_value2 =  top_pair2[1]

        #     if max_key1 * max_value1 >= n1 and max_key2 * max_value2 >= n2:
        #         dominant_ele1 = max_key1
        #         dominant_ele2 = max_key2
                
        #     if (max_value1 * 2 > n1) and (max_value2 * 2 > n2):
        #         if max_key1 == max_key2:
        #             return i 

        # return -1

    # Initialize variables based on your setup
        # nums_list = nums
        # n = len(nums_list)
        # to_split = n // 2
        
        # # FIX 1: Turn list into a Counter to get the global max_key
        # nums_counter = Counter(nums_list)
        # top_pair = nums_counter.most_common(1)[0] 
        # max_key = top_pair[0] 
        
        # # FIX 3: Wrap your logic in a loop using a standard index pointer 'i'
        # i = 0
        # while i < n - 1:
        #     arr1 = nums_list[0:i+1]
        #     arr2 = nums_list[i+1:len(nums_list)]  # Keep total length stable

        #     n1 = len(arr1)
        #     n2 = len(arr2)

        #     # FIX 2: Convert slices to Counter objects before calling .most_common()
        #     freq1 = Counter(arr1)
        #     freq2 = Counter(arr2)
        #     top_pair1 = freq1.most_common(1)[0]
        #     top_pair2 = freq2.most_common(1)[0]

        #     count1 = arr1.count(max_key)
        #     count2 = arr2.count(max_key)
            
        #     # Your condition checking if max_key dominates both arrays
        #     if count1 * 2 > n1 and count2 * 2 > n2:
        #         return i  # Return the index where this condition is met
        #     else:
        #         # Shift the index pointer based on your logic to check the next split
        #         if count1 * 2 > n1:
        #             i += 1 
        #         else:
        #             i += 1

        # return -1
        
        n = len(nums)
        
        # 1. Find the global dominant element (your exact strategy)
        global_counter = Counter(nums)
        top_pair = global_counter.most_common(1)[0]
        max_key = top_pair[0]
        total_max_count = top_pair[1] # Total times max_key appears in the whole array
        
        # 2. Tracks how many times max_key has appeared in arr1 so far
        count1 = 0
        
        # 3. Use a single loop to move the split point (replaces your while loop/slices)
        for i in range(0, n - 1):
            # Update the left count instantly without using arr1.count()
            if nums[i] == max_key:
                count1 += 1
                
            # The right count is just the leftover total (O(1) math instead of arr2.count())
            count2 = total_max_count - count1
            
            # Calculate subarray lengths instantly
            n1 = i + 1
            n2 = n - n1
            
            # Your exact dominance condition check
            if count1 * 2 > n1 and count2 * 2 > n2:
                return i
                
        return -1
