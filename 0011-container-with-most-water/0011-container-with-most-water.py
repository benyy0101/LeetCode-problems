class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1

        max_volume = 0

        while left < right:
            min_height = min(height[right], height[left])
            length = right - left
            volume = min_height * length
            max_volume = max(max_volume, volume)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_volume

        
        