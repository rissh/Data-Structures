
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        n = len(arr)
        hashMap = Counter(arr)

        return len(set(hashMap.values())) == len(hashMap.keys())
        
        '''
        d = {}
        for i in arr:
            d[i] = d.get(i, 0) + 1

        s = set()
        for i,j in d.items():
            if j in s:
                return False
            s.add(j)
        return True

        '''
        
