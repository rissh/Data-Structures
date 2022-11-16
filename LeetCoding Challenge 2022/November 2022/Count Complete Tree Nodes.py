
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        '''
        def pre(node):
            if not node:
                return 0
            return pre(node.left)+pre(node.right)+1
        return pre(root)
        '''
        
        if not root:
            return 0
        
        def lheight(node):
            if not node:
                return 0
            return 1+lheight(node.left)
        
        def rheight(node):
            if not node:
                return 0
            return 1+rheight(node.right)
        
        LeftSub,RightSub = lheight(root),rheight(root)
        
        if(LeftSub == RightSub):
            return (2**LeftSub) - 1
        else:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
            
