class Solution:
    def climbStairs(self, n: int) -> int:
        array = [1,2]
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n > 2:    
            for i in range(2,n):
                array.append(array[i-2]+array[i-1])
        return array[-1]
