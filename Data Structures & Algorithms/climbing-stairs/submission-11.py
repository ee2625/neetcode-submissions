class Solution:
    def climbStairs(self, n: int) -> int:
        count = {}
        def fib(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in count:
                return count[n]
            else:
                count[n] = fib(n-1) + fib(n-2)
            return count[n]
        return fib(n)