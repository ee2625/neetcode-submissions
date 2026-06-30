class Solution:
    def climbStairs(self, n: int) -> int:
        count = {1:1,2:2}
        def fib(n):
            if n in count:
                return count[n]
            else:
                count[n] = fib(n-1) + fib(n-2)
                return count[n]
        return fib(n)