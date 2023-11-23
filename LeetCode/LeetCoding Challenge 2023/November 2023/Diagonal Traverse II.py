
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        rows = len(nums)
        col = len(nums[0])

        visited = []
        for i in range(rows):
            for j in range(len(nums[i])):
                visited.append((i + j, j, nums[i][j]))

        ans = list(x[2] for x in sorted(visited))
        return ans
      
