
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        self.odd = 0
        self.res = 0
        counter = Counter()
        def dfs(v):
            if not v: return
            counter[v.val] += 1
            if counter[v.val] % 2: 
                self.odd += 1
            else:
                self.odd -= 1
            if not v.left and not v.right:
                if self.odd == 0 or self.odd == 1:
                    self.res += 1
            else:
                dfs(v.left)
                dfs(v.right)
            if counter[v.val]% 2:
                self.odd -= 1
            else:
                self.odd += 1
            counter[v.val] -= 1
        dfs(root)
        return self.res
      
