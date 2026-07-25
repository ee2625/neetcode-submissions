class Solution:
    def climbStairs(self, n: int) -> int:
        seen = {1:1, 2:2}
        def fib(a):
            if a in seen:
                return seen[a]
            else:
                seen[a] = fib(a-1) + fib(a-2)
                return seen[a]
        return fib(n)