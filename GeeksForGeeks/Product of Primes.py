
#User function Template for python3
from numpy import sqrt 
class Solution:
    def prime(self,n):
        if n==1 or n==0:
            return False
        if n==2 or n==3:
            return True
        if n%2==0 or n%3==0:
            return False
        for i in range(5,int(sqrt(n))+1,6):
            if n%i==0 or n%(i+2)==0:
                return False
        return True
        # code here
    def primeProduct(self, L, R):
        d=1
        for i in range(L,R+1):
            if self.prime(i):
                d=d*i
                d=d%(10**9+7)
        return d%(10**9+7)
        
