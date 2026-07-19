class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        min = float('inf')

        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            
            profit = max(profit, prices[i] - min)


        return profit