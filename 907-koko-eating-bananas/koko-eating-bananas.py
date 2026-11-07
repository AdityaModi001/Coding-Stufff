class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low = 1 
        high = max(piles)
        res = high
        def checker(mid):
            count = 0
            for pile in piles:
                # Equivalent to math.ceil(pile / mid) using integer division
                count += (pile + mid - 1) // mid 
            return count

        while low <= high:
            mid = (low + high)//2
            val = checker(mid)
            if val <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res