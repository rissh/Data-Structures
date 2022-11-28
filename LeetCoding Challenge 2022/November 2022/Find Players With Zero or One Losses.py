
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        a=defaultdict(int)
        seen=set()       
        zero,one=[],[] 
        for x in matches:
            seen.add(x[0])  
            seen.add(x[1])   
            a[x[1]] +=1   
            
        for y in seen:    
            if a[y]==0:   
                zero.append(y)
            if a[y]==1: 
                one.append(y)
        return[sorted(zero),sorted(one)] 
        
