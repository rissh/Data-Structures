
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        curr1=original
        curr2=cloned
        
        found = None
        while curr1:
            if not curr1.left:
                if curr1==target:
                    found=curr2
                curr1=curr1.right
                curr2=curr2.right
            else:
                temp1 = curr1.left
                temp2 = curr2.left
                
                while temp1.right and temp1.right!=curr1:
                    temp1=temp1.right
                    temp2=temp2.right
                
                if temp1.right==curr1:
                    temp1.right=None
                    temp2.right=None
                    if curr1 == target:
                        found=curr2
                    curr1=curr1.right
                    curr2=curr2.right
                else:
                    temp1.right=curr1
                    temp2.right=curr2
                    curr1=curr1.left
                    curr2=curr2.left
        return found
        
