class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Brute force, test between days 1 at a time to see which day gives
        # Highest return

        best = 0             

        for buy in range(len(prices)):
            for sell in range(buy + 1, len(prices)):
                profit = prices[sell] - prices[buy]
                best = max(best, profit)
        return best

