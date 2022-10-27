
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        
        n = len(A)
        
        def f(x_shift,y_shift):
            count = 0
            for r in range(n):
                for c in range(n):
                    if(0 <= c+x_shift < n and 0 <= r+y_shift < n and A[r+y_shift][c+x_shift] == 1 and B[r][c] == 1):
                        count += 1
            return count
        
        return max([f(x,y) for y in range(-n,n) for x in range(-n,n)])
      
