class Solution:
    def climbStairs(self, n: int) -> int:
        # exactly the same as fibonacci so our base case is a,b = 0,1
        if n <= 2:
            return n
        a,b = 1,2
        for _ in range(3,n+1):
            a,b= b, a+b
        return b
