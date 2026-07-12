class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        best = sum(weights)
        while left <= right:
            mid = (left + right) // 2
            dayday = 1
            total = 0
            for weight in weights:
                if total + weight <= mid:
                    total += weight
                else:
                    dayday += 1
                    total = weight
            if dayday <= days:
                best = min(best,mid)
                right = mid -1
            else:
                left = mid + 1
        return best
