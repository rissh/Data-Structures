
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        arr = [None] * (m+n)
        
        i, j, index, first = 0, 0, 0, True
        while i < n and j < m:
            if first:
                arr[index] = word1[i]
                first = not first
                i, index = i+1, index+1
            else:
                arr[index] = word2[j]
                first = not first
                j, index = j+1, index+1
        
        while i < n:
            arr[index] = word1[i]
            i, index = i+1, index+1
            
        while j < m:
            arr[index] = word2[j]
            j, index = j+1, index+1
        
        return ''.join(arr)
        
