
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(curr, currSum=0):
            if curr is None:
                return False
            
            currSum += curr.val
            
            if not curr.left and not curr.right and currSum == targetSum:
                return True
            
            return dfs(curr.left, currSum) or dfs(curr.right, currSum)
        return dfs(root)
      
