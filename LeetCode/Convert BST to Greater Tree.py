
# Method 1
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node:Optional[TreeNode],val:int)->int:
            if not node: return val
            node.val+=dfs(node.right,val)
            return dfs(node.left,node.val)
        sum=dfs(root,0)
        return root

# Method 2
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curSum = 0
        def dfs(node):
            if not node:
                return
            nonlocal curSum
            dfs(node.right)
            temp = node.val
            node.val += curSum
            curSum += temp
            dfs(node.left)
        dfs(root)
        return root
