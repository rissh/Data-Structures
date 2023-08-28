
class Solution:
    def frequencySort(self, s: str) -> str:
        '''
        c = Counter(list(s))
        
        c_list = sorted(c, key = lambda x: c[x],reverse = True)
        
        res = []
        for char in c_list:
            res.append(char*c[char])
            
        return "".join(res)    
        '''
        freq = {}
        for c in s:
            if c not in freq:
                freq[c] =1
            else:
                freq[c] +=1
        freq = sorted(freq.items(),key= lambda x: x[1],reverse= True)
        res = ""
        for item in freq:
            res += item[0]*item[1]
        return res
      
