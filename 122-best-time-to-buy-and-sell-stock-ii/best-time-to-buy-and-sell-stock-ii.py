class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # n = len(prices)
        # if n == 1:
        #     return 0
        # if min(prices) == prices[n-1]:
        #     return 0

        # to_pur = 0
        # start = 1
        # to_sell = 0
        # nums = 0
        # total_profit = 0

        # while nums < n:
        #     for i in range(start, n):
        #         if prices[i] < prices[to_pur]:
        #             to_pur = i  # Min = 1

        #     for to_sell in range(to_pur, n-1):
        #         if prices[to_sell] > prices[to_sell+1]:
        #             curr_profit = prices[to_sell] - prices[to_pur]
        #             total_profit += curr_profit
        #             break
        #         to_pur = to_sell + 1
        #     nums += 1
        # return total_profit

        profit = 0 
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
            
        return profit
