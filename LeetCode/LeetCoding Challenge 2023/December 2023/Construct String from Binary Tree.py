
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def f(node,s):
            if node is None:
                return ''
            elif node.left is None and node.right is None:
                return str(node.val)
            elif node.right is None:
                s+=str(node.val)+'('+f(node.left,s)+')'
            
            else:
                s+=str(node.val)+'('+f(node.left,s)+')('+f(node.right,s)+')'
            return s
        
        return f(root,"")

