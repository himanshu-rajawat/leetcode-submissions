# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_val = 0
        def dfs(node):
            if not node:
                return 0
            left_max = dfs(node.left)
            right_max = dfs(node.right)

            self.max_val = max(self.max_val, left_max+right_max+1)
            res = 1+max(left_max,right_max)
            return res
        dfs(root)
        return self.max_val - 1

        