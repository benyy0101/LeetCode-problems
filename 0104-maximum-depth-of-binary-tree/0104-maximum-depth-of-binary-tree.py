from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0
        
        qq = deque()
        qq.append([root,1])
        
        max_depth = -sys.maxsize
        
        while qq:
            node, depth = qq.popleft()
            if depth > max_depth:
                max_depth = depth
                
            if node.left != None:
                qq.append([node.left, depth+1])
                
            if node.right != None:
                qq.append([node.right, depth+1])
            
        return max_depth
            
        
        
        