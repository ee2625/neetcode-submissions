class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        left = 0
        for i in range(1,len(prices)):
            best = max(best,prices[i]-prices[left])
            if prices[left] > prices[i]:
                left = i
        return best