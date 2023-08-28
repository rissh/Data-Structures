
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaf(root):
            if root.left or root.right:
                if root.left:
                    for key in leaf(root.left):
                        yield key
                if root.right:
                    for key in leaf(root.right):
                        yield key
            else:
                yield root.val
        return list(leaf(root1)) == list(leaf(root2))
      
