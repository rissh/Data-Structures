
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        n1 = len(str1)
        n2 = len(str2)

        def isDivisor(l):
            if n1 % l or n2 % l:
                return False
            f1,f2 = n1 // l, n2 // l
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        for l in range(min(n1,n2),0,-1):
            if isDivisor(l):
                return str1[:l]

        return ""
      
