
class BSTIterator(object):

    def __init__(self, root):
        # get the in order tree node values
        def inorder(root):
            if not root:    return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        self.treenodes = inorder(root)
        
        
    def next(self):
        # pop out the current smallest int
        return self.treenodes.pop(0)
        

    def hasNext(self):
        # check if there are remaining int
        return len(self.treenodes) != 0
        
