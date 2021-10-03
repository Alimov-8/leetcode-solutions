# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # When the binary tree empty
        if root == None:
            return 0
        
        def tree_height_min(node):
            # The minimum depth of a binary tree is the number of nodes 
            # from the root node to the nearest leaf node.
            if node != None:
                if node.left == None and node.right == None:
                    return 1    
            elif node == None:
                return 100000  # max value
                        
            return 1 + min(tree_height_min(node.left), tree_height_min(node.right))
        
        return tree_height_min(root)
