
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:

        n = len(nums)
        hashMap = collections.Counter(nums)
        
        keys = sorted(hashMap.keys(), reverse = True)
        curr = 0
        total = 0

        for key in keys[:-1]:
            curr += hashMap[key]
            total += curr

        return total
      
