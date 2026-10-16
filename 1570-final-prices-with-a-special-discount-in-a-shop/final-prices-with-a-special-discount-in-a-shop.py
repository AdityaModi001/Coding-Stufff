import sys 

class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        # n = len(prices)
        # ans = []
        # for i in range(n): 
        #     discount = 0
        #     to_buy = prices[i]
        #     for j in range(i+1,n):
        #         if j > i and prices[j] <= prices[i]:
        #             discount = prices[j]
        #             break
        #         else:
        #             discount = 0 
        #     ans.append(to_buy - discount)
        # return ans

        # stack = []
        # n = len(prices)
        # for i in range(n-1,0,-1):
        #     stack.append(prices[i])
        n = len(prices)
        for i in range(n):
            to_buy = prices[i]
            get_discount = 0

            stack = []
            for k in range(n - 1, i, -1):
                stack.append(prices[k])
            j = i + 1 
            while j < n:
                e = stack.pop()
                if e <= to_buy:
                    get_discount = e
                    break
                else:
                    j += 1
            prices[i] = to_buy - get_discount
        
        return prices