# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0, True
            right, right_flag = dfs(node.right)
            left, left_flag = dfs(node.left)
            
            return max(right, left)+1, abs(right-left)<=1 and left_flag and right_flag
        
        h, flag = dfs(root)
        return flag
            