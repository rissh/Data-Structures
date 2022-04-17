
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def sortBST(node):
            if not node:    return []
            return sortBST(node.left) + [node.val] + sortBST(node.right)
            
        sorted_list = sortBST(root)
        ans = temp = TreeNode(sorted_list[0])
        for i in range(1, len(sorted_list)):
            temp.right = TreeNode(sorted_list[i])
            temp = temp.right
            
        return ans
      
