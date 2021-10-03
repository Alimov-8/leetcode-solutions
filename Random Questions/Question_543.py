# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.answer = 1
        
        def depth(node):
            if not node: return 0
            left = depth(node.left)
            right = depth(node.right)
            self.answer = max(self.answer, left + right + 1)
            return max(left, right) + 1
        
        depth(root)
        return self.answer - 1
        
        
