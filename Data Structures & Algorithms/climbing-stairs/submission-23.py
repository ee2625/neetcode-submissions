class Solution:
    def climbStairs(self, n: int) -> int:
        group = {1:1,2:2}
        def fib(n):
            if n in group:
                return group[n]
            group[n] = fib(n-1) + fib(n-2)
            return group[n]
        return fib(n)