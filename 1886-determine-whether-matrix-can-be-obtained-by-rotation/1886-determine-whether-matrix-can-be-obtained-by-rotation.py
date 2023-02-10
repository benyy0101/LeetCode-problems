class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        
        for _ in range(4):
            top, bottom = 0, len(mat) - 1
            
            while top < bottom:
                left, right = top, bottom
                
                for i in range(bottom - top):
                    topLeft = mat[top][left + i]
                    mat[top][left + i] = mat[bottom - i][left]
                    mat[bottom - i][left] = mat[bottom][right - i]
                    mat[bottom][right - i] = mat[top + i][right]
                    mat[top + i][right] = topLeft
                    
                top += 1
                bottom -= 1
                    
            if mat == target:
                return True
        
        return False
                    
                    
            