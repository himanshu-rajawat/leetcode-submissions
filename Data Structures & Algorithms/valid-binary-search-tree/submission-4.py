# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, maxValue, minValue):
            if not node:
                return True

            if not (minValue<node.val<maxValue):
                return False
            
            return validate(node.left,node.val,minValue) and validate(node.right,maxValue, node.val)

        return validate(root, float('inf'), float('-inf'))

        
        