
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if(root!=None and root.val in range(low,high+1)):
            if root.val==low:
                root.left=None
                root.right=self.trimBST(root.right,low,high)
            elif root.val==high:
                root.right=None
                root.left= self.trimBST(root.left,low,high)
            else:
                root.left=self.trimBST(root.left,low,high)
                root.right=self.trimBST(root.right,low,high)
        elif root!= None:
            if root.val>high:
                root=self.trimBST(root.left,low,high)
            else:
                root=self.trimBST(root.right,low,high)
        return root
      
