
#Back-end complete function Template for Python 3
from collections import Counter
class Solution:
    def transform(self, A, B): 
        #code here.
        lenA = len(A)
        lenB = len(B)
        
        op_req = 0
        
        if lenA != lenB:
            return -1
            
        if Counter(A) != Counter(B):
            return -1
        
      
        r = lenA-1
        i = lenB-1
        
        while( i >= 0):
            if (A[i] == B[r]):
                i-=1
                r-=1
            else:
                i-=1
                op_req += 1
        
            
        return op_req
      
