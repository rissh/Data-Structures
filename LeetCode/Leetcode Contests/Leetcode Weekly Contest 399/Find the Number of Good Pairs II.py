
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        n = len(nums1)
        m = len(nums2)
        hashMap = Counter(num * k for num in nums2)
        fact = defaultdict(int)

        res = 0
        for num in nums1:
            
            for i in range(1, int(math.sqrt(num)) + 1):
                
                if num % i == 0:
                    factor1, factor2 = i, num // i
                    res += hashMap[factor1]
                    
                    if factor1 != factor2:
                        res += hashMap[factor2]

        return res
      
