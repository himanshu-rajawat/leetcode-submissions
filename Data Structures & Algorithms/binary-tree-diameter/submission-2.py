# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0
            left_d, right_d = dfs(root.left), dfs(root.right)
            self.max_diameter = max(self.max_diameter, left_d+right_d)
            return 1+max(left_d, right_d)
        dfs(root)
        return self.max_diameter

        