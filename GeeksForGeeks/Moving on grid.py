
#User function Template for python3

class Solution:
	def movOnGrid(self, r, c):
		# code here
        r=r%7
        c=c%4
        
        if(c==0):
            c=4
            
           
        if(r==c and r>=1 and r<=4):
            return "ARYA"
            
        return "JON"
      
