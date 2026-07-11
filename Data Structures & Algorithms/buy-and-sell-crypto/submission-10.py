class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        best = -float('inf')
        for i in range(1,len(prices)):
            if prices[i] < prices[left]:
                left = i
            else:
                best = max(best,prices[i] - prices[left])
            
        


        if best == -float('inf'):
            return 0
        else:
            return best