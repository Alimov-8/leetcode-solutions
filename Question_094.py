# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        def inorderTraversal(self, root: TreeNode) -> List[int]:
            
            def traverse_in_order(node):
                if node is None: 
                    return []
                return(traverse_in_order(node.left) + 
                       [node.val] + 
                       traverse_in_order(node.right))
            return traverse_in_order(root)
