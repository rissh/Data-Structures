
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        HashMap = defaultdict(int)
        odd = 0 # Number of digits with odd count of occurance

        def dfs(curr):

            nonlocal odd
            if not curr:
                return 0

            HashMap[curr.val] += 1
            odd_change = 1 if HashMap[curr.val] % 2 == 1 else -1
            odd += odd_change

            if not curr.left and not curr.right:
                res = 1 if odd <= 1 else 0
                
            else:
                res = dfs(curr.left) + dfs(curr.right)

            odd -= odd_change
            HashMap[curr.val] -= 1
            return res
        
        return dfs(root)
        

        '''
        HashMap = defaultdict(int)
        odd = 0 # Number of digits with odd count of occurance

        def dfs(curr):

            nonlocal odd
            if not curr:
                return 0

            HashMap[curr.val] += 1
            odd_change = 1 if HashMap[curr.val] % 2 == 1 else -1
            odd += odd_change

            if not curr.left and not curr.right:

                res = 1 if odd <= 1 else 0
                odd -= odd_change
                HashMap[curr.val] -= 1
                return res

            res = dfs(curr.left) + dfs(curr.right)
            odd -= odd_change
            HashMap[curr.val] -= 1
            return res
        
        return dfs(root)
        '''
        
        
        '''
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

        '''
      
