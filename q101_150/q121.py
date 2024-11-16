class Solution:
    # Time: O(N)
    # Space: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        profit = 0 
        for price in prices: 
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit
