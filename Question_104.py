# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def tree_height(node):
            if node is None:
                return 0
            return 1 + max(tree_height(node.left), tree_height(node.right))
        return tree_height(root)
