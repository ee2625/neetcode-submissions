class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        seen = {}
        def path(a,b):
            if a == 1 or b == 1:
                return 1
            if (a,b) in seen:
                return seen[(a,b)]
            seen[(a,b)] = path(a,b-1) + path(a-1,b)
            return seen[(a,b)]
        return path(m,n)