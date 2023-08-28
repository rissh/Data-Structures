
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0

        self.dept = float("inf")
        self.dfs(root, 0)
        return self.dept

    def dfs(self, node, curr_dept):
        
        if not node:
            return

        if not node.right and not node.left:
            self.dept = min(self.dept,curr_dept + 1)

        self.dfs(node.right, curr_dept + 1)            
        self.dfs(node.left, curr_dept + 1)
