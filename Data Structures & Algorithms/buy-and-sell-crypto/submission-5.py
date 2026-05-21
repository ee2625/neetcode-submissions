class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        best = 0
        
        for price in prices:
            minimum = min(minimum, price)
            best = max(best, price - minimum)
        
        return best