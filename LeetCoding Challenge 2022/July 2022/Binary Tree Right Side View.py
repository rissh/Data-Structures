
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        l = defaultdict(int)
        
        def dfs(node,h):
            
            if not node:
                return
            
            if h not in l:
                l[h] = node.val
                
            dfs(node.right,h+1)
            dfs(node.left,h+1)
                
        dfs(root,0)
        
        return l.values()
        
