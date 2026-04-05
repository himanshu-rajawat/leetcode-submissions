# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        return self.in_order_traversal(root)

    def in_order_traversal(self, root):
        if not root:
            return "N"
        return str(root.val) +','+ self.in_order_traversal(root.left)+ ','+ self.in_order_traversal(root.right)

    def construct_from_string(self, str_val):
        if str_val == "N":
            return
        val_list = str_val.split(',')
        return TreeNode(int(val_list[0]), self.construct_from_string(', '.join(val_list[1:])) if len(val_list)>1 else self.construct_from_string(""), self.construct_from_string(', '.join(val_list[2:])) if len(val_list)>2 else self.construct_from_string("")) if val_list[0]!="N" else None

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        data_list = data.split(',')
        idx = 0
        def dfs():
            nonlocal idx
            if data_list[idx]=="N":
                idx+=1
                return
            node = TreeNode(int(data_list[idx]))
            idx+=1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()