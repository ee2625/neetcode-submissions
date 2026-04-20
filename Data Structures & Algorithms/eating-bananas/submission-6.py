class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high

        while low <= high:
            k = (low + high) // 2
            total_time = 0
            
            # Check how many hours this speed 'k' takes
            for p in piles:
                total_time += math.ceil(p / k)
            
            if total_time <= h:
                # Koko finished in time! Save this as a possible answer
                # and try to find an even SLOWER speed.
                res = k
                high = k - 1
            else:
                # Too slow! We must eat faster.
                low = k + 1
                
        return res