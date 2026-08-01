class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        left = 0 
        for i in range(1,len(prices)):
            while left < i and prices[left] >= prices[i]:
                left += 1
            best = max(best,prices[i]-prices[left])
        return best