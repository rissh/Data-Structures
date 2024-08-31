
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        res = []
        def f(node):
            if not node:
                return 

            for c in node.children:
                f(c)
            res.append(node.val)
            
        f(root)
        return res
      
