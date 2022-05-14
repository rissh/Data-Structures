
#User function Template for python3

class Solution:
	def MaxGold(self, matrix):
		# Code here
		if max(matrix[0]) == -1:
            return 0
        m, n = len(matrix), len(matrix[0])
        ans = max(0, max(matrix[0]))
        for i in range(m-2, -1, -1):
            for j in range(0,n):
                if matrix[i][j] != -1:
                    p = 0
                    p = max(p,matrix[i+1][j])
                    if j-1 >= 0:
                        p = max(p,matrix[i+1][j-1])
                    if j+1 < n:
                        p = max(p,matrix[i+1][j+1])
                    matrix[i][j] += p
        return max(matrix[0])
     
