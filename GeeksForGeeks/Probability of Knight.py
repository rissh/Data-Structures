
#User function Template for python3

class Solution:
	def findProb(self, N, start_x, start_y, steps):
	    curr=[]
        moves=[[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]]
        probability=[[0 for x in range(N)] for x in range(N)]
        probability[start_x][start_y]=1
        
        for k in range(steps):
            new=[[0 for x in range(N)] for i in range(N)]
            for i in range(N):
                for j in range(N):
                    if probability[i][j]!=0:
                        for x,y in moves:
                            if self.possible(i+x,j+y,N):
                                new[i+x][j+y]+=(probability[i][j]/8)
                                
                                
            probability=new
                    
                    
        pro=0           
        for i in range(N):
            for j in range(N):
                pro+=probability[i][j]
              
              
        return pro
                            
                            
        
    def possible(self,x,y,N):
        if x>-1 and x<N and y>-1 and y<N:
            return True
        return False
      
