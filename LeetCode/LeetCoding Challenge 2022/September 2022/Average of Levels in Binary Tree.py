
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        sums = defaultdict(float)
        nodes = defaultdict(int)
        
        def dfs(node,h):
            
            if not node:
                return
            dfs(node.left,h+1)
            dfs(node.right,h+1)
            
            sums[h] += node.val
            nodes[h] += 1
            
        dfs(root,0)
        output = []
        
        for i in range(len(sums)):
            output.append(sums[i]/nodes[i])
        return output
      
