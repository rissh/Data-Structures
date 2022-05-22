
#User function Template for python3

class Solution:
    def findAndReplace(self, s, q, index, sources, targets):
        # code here 
        ver=[True]*q
        for _ in range(q):
            pos=index[_]
            x=sources[_]
            y=targets[_]
            j=-1
            for i in range(pos,pos+len(x)):
                j+=1
                try:
                    if x[j]==s[i]:
                        continue
                    else:
                        ver[_]=False
                except:
                    ver[_]=False
        ans=""
        i=0
        j=0
        while i<len(s):
            if i==index[j]:
                if ver[j]==True:
                    i+=len(sources[j])
                    ans+=targets[j]
                else:
                    ans+=s[i]
                    i+=1
                j+=1
                if j>=q:
                    j-=1
            else:
                ans+=s[i]
                i+=1
        return ans
      
