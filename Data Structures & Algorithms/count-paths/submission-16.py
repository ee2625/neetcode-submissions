class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        seen = {}
        def fib(m,n):
            if m == 1 or n == 1:
                return 1
            elif (m,n) in seen:
                return seen[(m,n)]
            else:
                seen[(m,n)] = fib(m,n-1) + fib(m-1,n)
            return seen[(m,n)]
        return fib(m,n)
