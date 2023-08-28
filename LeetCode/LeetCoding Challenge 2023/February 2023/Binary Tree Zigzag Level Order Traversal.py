
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque([root])
        level = 0
        ans = []
        while q:
            level_nodes = []
            for _ in range(len(q)):
                curr = q.popleft()
                if level % 2 == 0:
                    level_nodes.append(curr.val)
                else:
                    level_nodes.insert(0, curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            ans.append(level_nodes)
            level += 1
        return ans
        
