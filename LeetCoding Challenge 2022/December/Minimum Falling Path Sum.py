
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        for row in reversed(range(len(A)-1)):
            for col in range(len(A[row])):
                if col == 0:
                    A[row][col] += min(A[row+1][col], A[row+1][col+1])
                elif col == len(A[row])-1:
                    A[row][col] += min(A[row+1][col], A[row+1][col-1])
                else:
                    A[row][col] += min(A[row+1][col], A[row+1][col-1], A[row+1][col+1])
        return min(A[0])
        
