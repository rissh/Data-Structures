
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        return self.f(root,0,low,high)

    def f(self,node,res,low,high):
        if not node:
            return res
                
        if node.val>=low and node.val<=high:
            res+=node.val
                
        res=self.f(node.left,res,low,high)
        res=self.f(node.right,res,low,high)
            
        return res
      
