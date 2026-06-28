class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights)-1
        max_vol = 0
        while start < end:
            left = heights[start]
            right = heights[end]
            max_vol = max(max_vol, (end-start)*min(left,right))
            if left < right:
                start += 1
            else:
                end -= 1
        return max_vol