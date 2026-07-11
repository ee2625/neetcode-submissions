class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        seen = {}
        def paths(a,b):
            if a == 1 or b == 1:
                return 1
            if (a,b) in seen:
                return seen[(a,b)]
            else:
                seen[(a,b)] = paths(a-1,b) + paths(a,b-1)
            return seen[(a,b)]
        return paths(m,n)
        