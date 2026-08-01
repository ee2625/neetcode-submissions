class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        best = 0
        while left <= right:
            width = right - left
            height = min(heights[left],heights[right])
            vol = width * height
            best = max(best,vol)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return best