
def f1(n):
    
    if n < 2:
        return False
    
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
        
    return True

def generate_numbers(mat, i, j):
    
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    numbers = []
    m, n = len(mat), len(mat[0])
    
    for dx, dy in directions:
        x, y = i, j
        
        num = mat[x][y]
        while 0 <= x < m and 0 <= y < n:
            
            numbers.append(num)
            x += dx
            y += dy
            
            if 0 <= x < m and 0 <= y < n:
                num = num * 10 + mat[x][y]
                
    return numbers

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        
        hashMap = {}
        n = len(mat)
        m = len(mat[0])
        
        for i in range(n):
            for j in range(m):
                numbers = generate_numbers(mat, i, j)
                
                for num in numbers:
                    
                    if num not in hashMap:
                        hashMap[num] = 0
                    hashMap[num] += 1
                    
        res = -1
        maxFreq = 0
        
        for num, freq in hashMap.items():
            
            if f1(num) and num > 10 and freq > maxFreq:
                res = num
                maxFreq = freq
                
            elif f1(num) and num > 10 and freq == maxFreq:
                res = max(res, num)
                
        return res
      
