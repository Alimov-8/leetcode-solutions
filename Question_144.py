# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        def traverse_in_preorder(node):
            if node is None: 
                return []
            return([node.val] + traverse_in_preorder(node.left) +  
                   traverse_in_preorder(node.right))
                   
        return traverse_in_preorder(root)
