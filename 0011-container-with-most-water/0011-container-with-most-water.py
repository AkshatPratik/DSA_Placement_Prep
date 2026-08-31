class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0 
        right = n - 1
        max_area = 0

        for i in range(n):
            h = min(height[left],height[right])
            width = right - left
            max_area = max(max_area,h*width)
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        return max_area