
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        n, m = len(matrix), len(matrix[0])
        res = []
        min_row = set()

        for r in range(n):
            min_row.add(min(matrix[r]))

        for c in range(m):
            curr_max = matrix[0][c]
            
            for r in range(n):
                curr_max = max(curr_max, matrix[r][c])

            if curr_max in min_row:
                res.append(curr_max)

        return res

