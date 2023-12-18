
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        n = len(grid)
        m = len(grid[0])
        
        arr = []
        for row in grid:
            for num in row:
                arr.append(num)
      
        hashMap = Counter(arr)
        
        repNum = 0
        for num, count in hashMap.items():
            if count == 2:
                repNum = num
                break
                
        missNum = 0
        for num in range(1, n * n + 1):
            if hashMap[num] == 0:
                missNum = num
                break

        return [repNum, missNum]
      
