# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")

        def dfs(node):
            if not node:
                return 0
            max_sum_left, max_sum_right = dfs(node.left), dfs(node.right)
            curr_max_path_sum = max(max_sum_left+node.val+max_sum_right, max_sum_left+node.val, node.val+max_sum_right, node.val)
            self.max_sum = max(self.max_sum, curr_max_path_sum)
            return max(max_sum_left+node.val, node.val+max_sum_right, node.val)
        dfs(root)
        return self.max_sum


        
        