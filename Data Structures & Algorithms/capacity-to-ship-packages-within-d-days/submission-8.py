class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        best = float('inf')
        while left <= right:
            mid = (left + right) // 2
            total = 0
            dayday = 1
            for weight in weights:
                if total + weight > mid:
                    dayday += 1
                    total = weight
                else:
                    total += weight
            if dayday <= days:
                best = min(best,mid)
                right = mid - 1
            else:
                left = mid + 1
        return best

