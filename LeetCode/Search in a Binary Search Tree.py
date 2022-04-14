
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.val == val:
            return root
        check = self.searchBST(root.left, val)
        if check:
            return check
        check = self.searchBST(root.right, val)
        if check:
            return check
        return None
      
