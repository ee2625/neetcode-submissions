class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        best = sum(weights)
        while left <= right:
            mid = (left + right) // 2
            days1 = 1
            total = 0
            for weight in weights:
                if total + weight > mid:
                    days1 += 1
                    total = 0
                total += weight
            if days1 > days:
                left = mid + 1
            else: 
                best = min(best,mid)
                right = mid - 1
        return best
            