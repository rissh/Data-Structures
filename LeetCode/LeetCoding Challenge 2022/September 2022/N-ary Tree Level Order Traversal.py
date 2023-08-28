
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        res = defaultdict(list)
        
        def dfs(node,level):
            if not node:
                return
            
            res[level].append(node.val)
            for x in node.children:
                dfs(x,level+1)
                
        dfs(root,0)
        
        return [x for i,x in res.items()]
      
