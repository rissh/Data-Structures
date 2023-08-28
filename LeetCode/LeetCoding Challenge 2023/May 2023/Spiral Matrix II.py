
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top,bottom,left,right,num = 0,n-1,0,n-1,1
        d = 0
        res = [[0]*n for i in range(n)]
        
        while left <= right and top <= bottom:
            if d == 0:
                for i in range(left,right+1):
                    res[top][i] = num
                    num += 1
                top+=1
            elif d == 1:
                for i in range(top,bottom+1):
                    res[i][right] = num
                    num += 1
                right-=1
            elif d == 2:
                for i in range(right,left-1,-1):
                    res[bottom][i] = num
                    num += 1
                bottom-=1
            elif d == 3:
                for i in range(bottom,top-1,-1):
                    res[i][left] = num
                    num += 1
                left+=1
            d = (d+1)%4
            
        return res
        
