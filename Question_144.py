# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        def traverse_pre_order(node):
            if node is None: 
                return []
            return([node.val] + traverse_pre_order(node.left) +  
                   traverse_pre_order(node.right))
                   
        return traverse_pre_order(root)
