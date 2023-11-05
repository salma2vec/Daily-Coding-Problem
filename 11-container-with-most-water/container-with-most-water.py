class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            h = min(height[left], height[right])
            width = right - left
            area = h * width
            max_area = max(max_area, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area        