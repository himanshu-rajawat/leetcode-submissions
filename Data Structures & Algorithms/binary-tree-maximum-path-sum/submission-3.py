# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')

        def dfs(node):
            nonlocal maxSum
            if not node:
                return 0
            left_sum, right_sum = dfs(node.left), dfs(node.right)
            maxSum = max(maxSum, left_sum+right_sum+node.val, max(left_sum, right_sum) + node.val, node.val)

            return max(max(left_sum, right_sum) + node.val, node.val)
        dfs(root)
        return maxSum

        
        