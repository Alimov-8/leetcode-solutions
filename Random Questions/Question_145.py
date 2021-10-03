# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
            
            def traverse_post_order(node):
                if node is None: 
                    return []
                return(traverse_post_order(node.left) + 
                       traverse_post_order(node.right)) + [node.val]
            return traverse_post_order(root)
