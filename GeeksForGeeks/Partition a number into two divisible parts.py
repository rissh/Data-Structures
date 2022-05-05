
#User function Template for python3
class Solution:
    def stringPartition(ob,S,a,b):
        # Code here
        l=""
        for i in range(1,len(S)):
            x=S[:i]
            y=S[i:]
            
            if int(x)%a==0 and  int(y)%b==0:
                l+=x
                l+=" "
                l+=y
                return l
        l+="-1"
        
        return l;
      
