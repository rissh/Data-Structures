
class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        
        n,m,l = len(s1),len(s2),len(s3)
        res = 0
        
        if s1[0] != s2[0] or s2[0] != s2[0]:
            return -1
        
        i = 0
        while i < min(n, m, l) and s1[i] == s2[i] and s2[i] == s3[i]:
            i += 1

        res = n + m + l - 3 * i

        if i == 0:
            return -1

        return res
    