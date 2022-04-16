
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node:Optional[TreeNode],val:int)->int:
            if not node: return val
            node.val+=dfs(node.right,val)
            return dfs(node.left,node.val)
        sum=dfs(root,0)
        return root
      
