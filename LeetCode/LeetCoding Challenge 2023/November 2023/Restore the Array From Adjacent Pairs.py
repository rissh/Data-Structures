
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        hashMap=defaultdict(list)

        for a,b in adjacentPairs:
            hashMap[a]+=b,
            hashMap[b]+=a,
        
        head,tail=[x for x in hashMap if len(hashMap[x])==1]
        prev,cur,res=None,head,[head]

        while cur!=tail:
            res+=[x for x in hashMap[cur] if x !=prev]
            prev,cur=cur,res[-1]

        return res
      
