class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        numerator = math.factorial(m+n-2)
        denominator = math.factorial(m-1)*math.factorial(n-1)
        return numerator // denominator
