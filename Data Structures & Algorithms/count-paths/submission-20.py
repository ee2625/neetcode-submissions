class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        seen = {}
        def fib(a,b):
            if a == 1 or b == 1:
                return 1
            elif (a,b) in seen:
                return seen[(a,b)]
            else:
                seen[(a,b)] = fib(a,b-1) + fib(a-1,b)
                return seen[(a,b)]
        return fib(m,n)
