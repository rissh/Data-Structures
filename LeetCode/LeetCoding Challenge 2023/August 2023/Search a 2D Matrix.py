
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n = len(matrix)
        m = len(matrix[0])
        
        low = 0
        high = m*n - 1
        
        while(low <= high):
            
            mid = (low+high) // 2
            num=matrix[mid//m][mid%m]
            
            if(num == target):
                return True
            
            elif(num < target):
                low = mid + 1
                
            else:
                high = mid - 1
        return False
