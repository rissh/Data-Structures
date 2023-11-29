
class Solution:
    def areSimilar(self, matrix: List[List[int]], k: int) -> bool:
        
        n = len(matrix)
        col = len(matrix[0])
        shift = k % col
        i = 0

        while i < n:
            if matrix[i] != matrix[i][-shift:] + matrix[i][:-shift]:
                return False
            i += 1

        return True
    