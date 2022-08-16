
#User function Template for python3

class Solution:
	def FactDigit(self, n):
		# Code hereb=[]
        n = N 
        lst=[ ] 
        for i in range(9,0,-1):
            ans = 1
            for j in range(i,0,-1):
                ans*=j 
            lst.append(ans) 
        x=0
        ans = [ ]
        while(n!=0):
            if (n<lst[x]):
                x+=1 
                continue 
            n-=lst[x]
            ans.append(9-x) 
        ans.reverse() 
        return ans
      
