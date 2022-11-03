
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        D = defaultdict(int)
        res = 0
        p = False

        for x in words:
            D[x] += 1
        
        for x in list(D.keys()):
            if x[0] == x[1]:
                if D[x]%2 == 1: p = True
                res += (D[x]//2)*4
            else:
                res += 2*min(D[x],D[x[::-1]])

        if p:
            return res + 2
            
        return res
        
