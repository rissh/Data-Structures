
class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        n = len(matrix)
        m = len(matrix[0])
        
        answer = [row[:] for row in matrix]  

        maxValues = [0] * m

        for j in range(m):
            maxVal = matrix[0][j]
            for i in range(1, n):
                maxVal = max(maxVal, matrix[i][j])
            maxValues[j] = maxVal

        for i in range(n):
            for j in range(m):
                if answer[i][j] == -1:
                    answer[i][j] = maxValues[j]

        return answer
      
