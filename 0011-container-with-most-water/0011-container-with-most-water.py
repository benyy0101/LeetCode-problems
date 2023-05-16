import sys

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_vol = -sys.maxsize
        
        while left < right:
            length = right - left
            
            cur_vol = length * min(height[right], height[left])
            
            if cur_vol > max_vol:
                max_vol = cur_vol
                
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        
        return max_vol

        
        