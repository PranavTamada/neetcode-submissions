class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = float("-inf")
        leftmax = heights[0]
        n = len(heights)
        rightmax = heights[n-1]
        left = 0
        right = n-1
        while left < right:
            water = (right - left)*min(rightmax,leftmax)
            max_water = max(max_water,water)
            if leftmax < rightmax:
                left += 1
                leftmax = max(leftmax,heights[left])
            else:
                right -= 1
                rightmax = max(rightmax,heights[right])
        return max_water

        