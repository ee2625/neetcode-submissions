class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1,amount+1):
            for num in coins:
                if i - num >= 0:
                    dp[i] = min(dp[i],dp[i - num] + 1)
        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]