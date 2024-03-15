
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = 0
        hashMap = collections.Counter(nums)
        
        maxFreq = max(hashMap.values())
        
        for i in hashMap.values():
            if i == maxFreq:
                res += 1
                
        ans = res * maxFreq
                
        return ans

