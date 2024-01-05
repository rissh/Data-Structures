
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:

        hashMap = collections.Counter(nums)

        ans = []
        for k,v in hashMap.items():
            for i in range(v):
                if i >= len(ans):
                    ans.append([])
                ans[i].append(k)

        return ans
    
    
    
    '''
        n = len(nums)
        hashMap = defaultdict(int)
        res = []
        
        for n in nums:
            row = hashMap[n]
            if len(res) == row:
                res.append([])

            res[row].append(n)
            hashMap[n] += 1

        return res
        
    '''
  
