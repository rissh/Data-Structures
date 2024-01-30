
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def LeafNodes(root):

            nums = []

            def traverse(node):
                if node is None:
                    return 

                traverse(node.left)
                if node.left is None and not node.right:
                    nums.append(node.val)
                traverse(node.right)

            traverse(root)
            return nums

        return LeafNodes(root1) == LeafNodes(root2)


'''
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(root,leaf):

            if not root:
                return 

            if not root.left and not root.right:
                leaf.append(root.val)
                return 

            dfs(root.left, leaf)
            dfs(root.right, leaf)

        leaf1, leaf2 = [], []
        dfs(root1, leaf1)
        dfs(root2, leaf2)

        return leaf1 == leaf2

'''        

'''
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def leaf(root):

            if root.left or root.right:

                if root.left:

                    for key in leaf(root.left):
                        yield key

                if root.right:

                    for key in leaf(root.right):
                        yield key

            else:
                yield root.val

        return list(leaf(root1)) == list(leaf(root2))

'''
