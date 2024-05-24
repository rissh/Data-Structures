
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:

        self.res = 0

        def dfs(curr):

            if not curr:
                return [0, 0]   #[Size, Coin]

            leftSize, leftCoin = dfs(curr.left)   
            rightSize, rightCoin = dfs(curr.right)    

            size = 1 + leftSize + rightSize
            coins = curr.val + leftCoin + rightCoin

            self.res += abs(size - coins)
            return [size, coins]

        dfs(root)
        return self.res 
