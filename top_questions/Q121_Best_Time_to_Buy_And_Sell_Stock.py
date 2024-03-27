class Solution:
    # Time: O(N)
    # Space: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        minPrice = sys.maxsize
        for i in range(len(prices)): 
            minPrice = min(minPrice, prices[i])
            profit = max(profit, prices[i] - minPrice)
        return profit
