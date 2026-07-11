class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        seen = {}
        def unique(a,b):
            if a == 1 or b == 1:
                seen[(a,b)] = 1
            if (a,b) in seen:
                return seen[(a,b)]
            else:
                seen[(a,b)] = unique(a-1,b) + unique(a,b-1)
            return seen[(a,b)]
        return unique(m,n)