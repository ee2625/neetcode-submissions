class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1
        best = 0
        for height in heights:
            width = right - left
            height = min(heights[left],heights[right])
            water = width * height
            best = max(best,water)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return best 