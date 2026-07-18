class Solution:
    def climbStairs(self, n: int) -> int:
        seen = {1:1,2:2}
        def fib(n):
            if n in seen:
                return seen[n]
            else:
                seen[n] = fib(n-1) + fib(n-2)
            return seen[n]
        return fib(n)
