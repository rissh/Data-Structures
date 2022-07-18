
#Function to return the ceil of given number in BST.

class Solution:
    def findCeil(self,root, inp):
        # code here
        if root == None:
            return 
        return self.inorder(root, inp, -9999999)
        
    def inorder(self, root, inp, ceil):
        if root != None:
            ceil = self.inorder(root.left, inp, ceil)
            if ceil != -9999999:
                return ceil
            if root.key >= inp:
                ceil = root.key
                return ceil
            ceil = self.inorder(root.right, inp, ceil)
        return ceil
        
